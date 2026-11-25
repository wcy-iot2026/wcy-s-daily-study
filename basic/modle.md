# Python 模块与导入：学习笔记

> 由几轮问答整理而来，涵盖 `sys.modules` 缓存、导入时字典变长的原因，以及三条导入优化建议。文中所有输出均为本机实测（Python 3.13）。

---

## 一、模块与包的基础

### 1.1 什么是模块

- 一个 `.py` 文件就是一个模块；`math`、`json` 是内置模块，`numpy` 是第三方模块。
- 一个带 `__init__.py` 的文件夹是「包」，包里可以有子模块（如 `json.decoder`）。
- `import math` 时，Python 找到源码（或内置实现），执行顶层代码，创建一个 **module 对象**供你使用。

### 1.2 模块里有什么

模块对象内部是一个字典 `__dict__`，存着「名字 → 对象」：

- 变量 / 常量：`math.pi`、`math.e`
- 函数：`math.sqrt`、`json.dumps`
- 类：`json.JSONDecoder`
- 子模块：`json.decoder`
- 元信息：`__name__`、`__file__`、`__doc__`、`__cached__`

```python
import math
print(dir(math))   # 列出所有名字
print(vars(math))  # 直接看那个字典
```

实测：`math` 中非下划线开头的名字有 62 个。

---

## 二、sys.modules：已加载模块的登记表

### 2.1 它是什么

`sys.modules` 是 Python 自带的一个**字典**，专门记录「当前程序里已经加载了哪些模块」：

| 模块名（键） | 模块对象（值） |
| --- | --- |
| `'sys'` | `<module 'sys'>` |
| `'math'` | `<module 'math'>` |
| `'numpy'` | `<module 'numpy'>` |

- 它不是你创建的，Python 一启动就自带。
- 启动时不是空的，已经登记了约 100 个基础模块（实测 102 个）。

### 2.2 为什么导入会自动加进去

这是 Python 设计好的规则：`import` 这个动作本身就包含「写登记表」这一步。

1. 先查表：没有 → 找文件、执行顶层代码。
2. 模块初始化时若又 `import` 了依赖，依赖也会被登记。
3. 每个成功加载的模块，都以「模块名 → 模块对象」写进表里。

作用：
- 避免重复执行模块顶层代码（省时间、防副作用）。
- 保证全局只有一份：`import math` 无论写多少次，拿到的都是同一个对象。

### 2.3 写法哪些固定、哪些自由

```python
import sys
module_dict = sys.modules
```

- `sys`、`modules` 是 Python 规定的固定名字，不能改拼写（`sys.module` 少个 `s` 就错）。
- `module_dict` 是你自己的变量名，随便起。
- `module_dict is sys.modules` → `True`，是同一个字典的别名，不是复制。

### 2.4 怎么用它

它是字典，**不是函数，不能加括号调用**（`sys.modules()` 会报 `TypeError: 'dict' object is not callable`）。先 `import sys`，然后按字典操作：

```python
import sys

len(sys.modules)                  # 数有多少模块 -> 102
'math' in sys.modules             # 查登记了没   -> True
m = sys.modules['math']           # 取出模块对象
print(m.sqrt(9))                  # 直接用      -> 3.0
list(sys.modules.keys())[:5]      # 看前 5 个名字
```

实测前 5 个模块名：`['sys', 'builtins', '_frozen_importlib', '_imp', '_thread']`

### 2.5 为什么 `len(module_dict)` 会变大

```python
import sys
module_dict = sys.modules          # 引用赋值，指向同一张表
print(len(module_dict))            # 加入之前
import numpy
print(len(module_dict))            # 变大
```

原因有两点：

1. `module_dict` 就是 `sys.modules` 本身，表里变多它自然变多。
2. `import numpy` 不只是加一个键——numpy 初始化时会连带导入 `numpy._core`、`numpy.linalg` 等一堆依赖，每个都登记一行。

实测（本机未装 numpy，用 `statistics` 演示等效机制）：

```
导入 statistics 后新增 6 条：
  statistics, _statistics, fractions, decimal, _decimal, numbers
之前 102 -> 之后 108
```

注意：
- 重复 `import` 同一个模块不会再增加（命中缓存）。
- `import numpy as np` 也只登记一次，键仍是 `'numpy'`。
- 想拿不随导入变化的快照，用 `module_dict = sys.modules.copy()`。

---

## 三、三条导入优化建议

> 以下三条来自截图笔记，每条都附代码和本机实测结果。

### 3.1 import 整个包：函数过多时导入慢

**现象**：写 `import 包名` 时，Python 会执行该包的 `__init__.py`；如果里面又导入了几十个子模块，它们会被全部加载一遍，耗时明显。

实测：造一个包，`__init__.py` 里导入 40 个子模块，对比两种写法（每次全新进程）：

```python
import bigpkg              # 写法 A：导入整个包
from smallpkg import m39   # 写法 B：只导入需要的子模块
```

```
导入整个包       ms: 24.696 / 22.083
按需导入子模块   ms:  1.103 /  1.181
```

慢了约 20 倍。改进：

```python
from bigpkg import m39   # 只要这一个
```

> 注意：如果包的 `__init__.py` 本身就写满了 `import`，这招效果有限，取决于包作者的组织方式。

### 3.2 延迟导入：用到时才 import

把 `import` 从文件开头挪到函数内部，函数被调用时才加载：

```python
import sys
print('调用前 decimal 在表里:', 'decimal' in sys.modules)  # False

def calc():
    import decimal          # 延迟导入
    return decimal.Decimal('1.1') + decimal.Decimal('2.2')

print(calc())                                            # 3.3
print('调用后 decimal 在表里:', 'decimal' in sys.modules)  # True
```

实测印证：调用前表里没有 `decimal`，调用后才出现。

**缺点**（截图原话）：不在文件开头导入，不利于管理。

- 看文件开头看不出依赖了什么。
- PEP 8 要求 `import` 写在顶部。
- 依赖藏在函数里，维护时容易漏看。

适用：确实很重、且不一定每次都用得上的模块，不要滥用。

### 3.3 抽离循环导入的部分到另一个模块

**循环导入**：A 导 B，B 又回头导 A，两边都没初始化完就报错。

```python
# a.py
from b import func_b
def func_a(): return 'A-' + func_b()

# b.py
from a import func_a      # 回头导 a，报错
def func_b(): return 'B-' + func_a()
```

运行 `import a` 实测：

```
ImportError: cannot import name 'func_a' from 'a'
```

原因：`a` 刚开始加载、还没定义出 `func_a`，`b` 就来拿，自然拿不到。

**解决办法**：把两边互相要用的公共部分抽到第三个模块 `c.py`：

```python
# c.py          ← 公共部分
def shared(x): return 'shared-' + str(x)

# a2.py
from c import shared
def func_a(): return 'A-' + shared(1)

# b2.py
from c import shared
def func_b(): return 'B-' + shared(2)
```

依赖关系从 `a ↔ b`（互相指）变成 `a → c ← b`（都指向公共模块），循环断开。实测：

```
退出码: 0
A-shared-1
B-shared-2
```

---

## 四、总结

| 主题 | 关键点 |
| --- | --- |
| 模块 | 一个 `.py` 文件；内含变量、函数、类、子模块，都放在 `__dict__` 里 |
| `sys.modules` | Python 自带的「已加载模块登记表」，字典，名字 → 模块对象 |
| 长度变大的原因 | `module_dict` 是同一张表；`import` 自动把模块及依赖登记进去 |
| ① 整包导入 | 函数多时慢，尽量按需 `from ... import ...` |
| ② 延迟导入 | 用到才加载，但不利管理，别滥用 |
| ③ 循环导入 | 抽离公共代码到第三模块，把双向依赖改成单向 |

三条建议的共同目标：**让导入更快、更清晰、不出错**。
