# 错题：混淆 set.add() 和 list.append()

## 分类
Python 基础

## 标签
`#set` `#list` `#add` `#append` `#extend`

## 当时犯的错误
误以为集合可以使用 `.append()`，列表可以使用 `.add()`，写完代码直接报错。

## 正确知识点
1. **`set.add(x)`**
   - 属于集合 set 的方法
   - 作用：添加单个元素，自动去重；集合无序
   - ❗ 集合没有 `.append()`

2. **`list.append(x)`**
   - 属于列表 list 的方法
   - 作用：在列表末尾，完整追加一个对象
   - 如果传入列表，会嵌套进去

3. **`list.extend(x)`**
   - 列表批量追加，把传入序列拆开，逐个放入列表

## 测试代码
```python
# 集合
s = set()
s.add(1)
s.add(99)
print(s)

# 列表 append
lst1 = []
lst1.append(5)
lst1.append([6, 7])
print(lst1)  # [5, [6, 7]]

# 列表 extend
lst2 = []
lst2.extend([6, 7])
print(lst2)  # [6, 7]
add:set add append错题
