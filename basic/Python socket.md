# Python socket 网络通信：知识点与易错点

> 整理日期：2026-11-26  
> 主题：服务端 / 客户端 TCP 通信，`socket` 的 `bind`、`listen`、`accept`、`connect`、`send`、`recv`，以及实际代码中的易错点。

---

## 目录

- [一、核心理解](#一核心理解)
- [二、六个步骤](#二六个步骤)
- [三、重要知识点](#三重要知识点)
- [四、完整代码模板](#四完整代码模板)
- [五、易错点总表](#五易错点总表)
- [六、一句话速记](#六一句话速记)

---

## 一、核心理解

socket 网络通信就像“打电话”：

| 角色 | 类比 | 动作 |
|---|---|---|
| 服务端 | 客服中心 | 先开机、占一个电话号码、等待别人打进来 |
| 客户端 | 打电话的人 | 主动拨号，接通后说话、听回复 |

一句话：

> **服务端先监听，客户端后连接；连接建立后，双方才能收发数据。**

所以运行顺序必须是：

1. 先运行 `server.py`
2. 再运行 `client.py`

如果客户端先运行，服务端还没监听，就会报 `ConnectionRefusedError`。

---

## 二、六个步骤

你截图里的编号对应完整通信流程：

| 步骤 | 所在端 | 代码 | 作用 |
|---|---|---|---|
| 第一步 | 服务端 | `socket()` / `bind()` / `listen()` | 创建服务、绑定地址端口、开始监听 |
| 第二步 | 客户端 | `socket()` / `connect()` | 创建客户端、连接服务端 |
| 第三步 | 客户端 | `encode()` / `send()` | 把字符串转成字节并发送 |
| 第四步 | 服务端 | `accept()` / `recv()` / `decode()` | 接收连接、接收数据、解码打印 |
| 第五步 | 服务端 | `encode()` / `send()` | 服务端回发数据 |
| 第六步 | 客户端 | `recv()` / `decode()` | 客户端接收服务端回复 |

核心对应关系：

```text
客户端 connect()  ←→  服务端 accept()
客户端 send()     ←→  服务端 recv()
服务端 send()     ←→  客户端 recv()
```

**一边 send，另一边必须有对应的 recv。**

---

## 三、重要知识点

### 1. `socket.socket(AF_INET, SOCK_STREAM)`

```python
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

- `AF_INET`：使用 IPv4 地址
- `SOCK_STREAM`：使用 TCP 协议，字节流模式

TCP 的特点是：**先建立连接，再传数据**，比较稳定。

---

### 2. `bind(("0.0.0.0", 55555))`

```python
server.bind(("0.0.0.0", 55555))
```

- `bind()`：把服务端绑定到某个 IP 和端口
- `"0.0.0.0"`：监听本机所有网卡地址
- `55555`：端口号

端口范围：

- `0 ~ 65535`
- `0` 一般不手动使用
- `1024` 以下很多是系统端口，普通练习用大端口，比如 `55555`

注意：

```text
0.0.0.0 是服务端“监听所有地址”
127.0.0.1 是客户端“连接本机”
```

如果客户端和服务端在同一台电脑：

```python
server.bind(("0.0.0.0", 55555))
client.connect(("127.0.0.1", 55555))
```

如果不在同一台电脑，客户端要写服务端的真实 IP：

```python
client.connect(("服务端IP", 55555))
```

---

### 3. `listen(5)`

```python
server.listen(5)
```

让服务端进入监听状态，等待客户端连接。

括号里的 `5` 表示等待连接队列长度，不是说最多只能连接 5 个客户端。

---

### 4. `accept()` 返回两个值

```python
client_socket_obj, client_address = server.accept()
```

`accept()` 会返回一个二元组：

| 返回值 | 含义 |
|---|---|
| `client_socket_obj` | 专门和这个客户端通信的 socket 对象 |
| `client_address` | 客户端地址和端口 |

关键区分：

```text
server            = 监听员，只负责等待连接
client_socket_obj = 通信员，负责和客户端收发数据
```

所以服务端接收和发送要用：

```python
client_socket_obj.recv(...)
client_socket_obj.send(...)
```

不要用：

```python
server.recv(...)   # 错
server.send(...)   # 错
```

---

### 5. `encode()` 和 `decode()`

网络传输的是 **bytes**，不是 Python 的普通字符串 `str`。

发送前：

```python
send_data = "你好".encode("utf-8")
```

接收后：

```python
res_data = data.decode("utf-8")
```

对应关系：

```text
str  →  encode()  →  bytes  →  网络传输  →  bytes  →  decode()  →  str
```

如果忘记编码：

```python
client.send("你好")   # TypeError
```

会报：

```text
TypeError: strings must be encoded before sending
```

---

### 6. `send()` / `sendall()`

```python
client.send(send_data)
```

小数据练习时通常能用。

更推荐：

```python
client.sendall(send_data)
```

区别：

- `send()` 不保证一次性把所有数据都发完
- `sendall()` 会尽量把数据全部发送完

初学阶段两者都能跑，但写 `sendall()` 更稳。

---

### 7. `recv(1024)`

```python
res_data = client.recv(1024)
```

表示一次最多接收 `1024` 字节。

注意：

- `recv()` 是**阻塞的**
- 没有数据来，程序会停在这一行等
- `1024` 是缓冲区大小，不代表一定刚好收到 1024 字节

所以如果客户端写了：

```python
res_data = client.recv(1024)
```

服务端必须有对应的：

```python
client_socket_obj.send(send_data)
```

否则客户端会一直卡在 `recv()`。

---

### 8. `connect()` 和 `accept()` 是一对

客户端：

```python
client.connect(("127.0.0.1", 55555))
```

服务端：

```python
client_socket_obj, client_address = server.accept()
```

客户端主动连接，服务端被动接受。

如果服务端没有先运行到 `accept()`，客户端连接可能会失败或等待。

---

### 9. try / except 的作用

```python
try:
    ...
except Exception as e:
    print(e)
```

作用：捕获网络运行时错误，避免程序直接崩溃。

但你截图里的客户端：

```python
client.connect(("127.0.0.1", 55555))
```

写在 `try` 外面。

所以如果服务端没启动，`connect()` 报 `ConnectionRefusedError`，这个 `except` **接不到**。

更稳的写法是把 `connect()` 也放进 `try`：

```python
try:
    client.connect(("127.0.0.1", 55555))
    ...
except Exception as e:
    print(e)
```

---

### 10. 当前代码只能服务一个客户端一次

你现在的流程是：

```text
服务端 accept 一次
接收一次
发送一次
结束
```

所以它只能完成一轮通信。

如果想让一个客户端连续说多句话，要在连接成功后循环：

```python
while True:
    data = client_socket_obj.recv(1024)
    ...
```

如果想服务多个客户端，要在外面循环 `accept()`：

```python
while True:
    conn, addr = server.accept()
    # 处理这个客户端
```

多个客户端同时通信，还要进一步用多线程或多进程。

---

## 四、完整代码模板

### server.py

```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 55555))
server.listen(5)
print("服务端加载成功.....")

try:
    client_socket_obj, client_address = server.accept()
    print("客户端已连接:", client_address)

    res_data = client_socket_obj.recv(1024).decode("utf-8")
    print("收到客户端:", res_data)

    send_data = "服务端向客户端发送的数据".encode("utf-8")
    client_socket_obj.sendall(send_data)

except Exception as e:
    print("服务端出错:", e)

finally:
    server.close()
```

---

### client.py

```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(("127.0.0.1", 55555))
    print("客户端连接成功")

    send_data = "客户端向服务端发送数据".encode("utf-8")
    client.sendall(send_data)

    res_data = client.recv(1024).decode("utf-8")
    print("收到服务端:", res_data)

except Exception as e:
    print("客户端出错:", e)

finally:
    client.close()
```

运行方式：

1. 打开一个终端，运行：

```bash
python server.py
```

2. 再打开另一个终端，运行：

```bash
python client.py
```

---

## 五、易错点总表

| # | 错误写法 / 现象 | 正确写法 / 原因 |
|---|---|---|
| 1 | 先运行客户端 | 必须先运行服务端，再运行客户端 |
| 2 | `client.connect(("0.0.0.0", 55555))` | 客户端连 `127.0.0.1` 或服务端真实 IP，`0.0.0.0` 是服务端监听地址 |
| 3 | 两端端口不一致 | 服务端 `bind` 和客户端 `connect` 端口必须一样 |
| 4 | `send("你好")` | 要用 `"你好".encode("utf-8")` |
| 5 | `print(res_data)` 收到 `b'...'` | 用 `res_data.decode("utf-8")` |
| 6 | `print(send_data)` 看见一堆 `b'\xe5...'` | 这是 bytes，正常；想看中文用 `decode()` |
| 7 | `server.recv()` / `server.send()` | 收发要用 `client_socket_obj` |
| 8 | 客户端卡在 `recv()` | 服务端没有对应的 `send()`，或没执行到 |
| 9 | 服务端卡在 `accept()` | 客户端还没连接，或连接地址端口不对 |
| 10 | `ConnectionRefusedError` | 服务端没启动、端口不一致、IP 写错 |
| 11 | `Address already in use` | 端口被占用，换端口或关掉旧程序 |
| 12 | `TypeError: strings must be encoded` | 忘写 `encode()` |
| 13 | `UnicodeDecodeError` | 编码和解码方式不一致，比如一边 gbk 一边 utf-8 |
| 14 | `connect()` 写在 `try` 外 | 连接失败时 `except` 接不到 |
| 15 | 以为 `listen(5)` 是最多 5 个客户端 | 它只是等待连接队列长度 |
| 16 | 想多个客户端却只 `accept()` 一次 | 要用循环反复 `accept()` |
| 17 | 想多轮聊天却只收发一次 | 要在已连接对象上循环 `recv/send` |

---

## 六、一句话速记

- **服务端四件套**：`socket()` → `bind()` → `listen()` → `accept()`
- **客户端三件套**：`socket()` → `connect()` → `send()/recv()`
- **发送前 encode，接收后 decode**
- **server 只监听，conn 才收发**
- **一边 send，另一边必须 recv**
- **recv / accept 都会阻塞**
- **先开服务端，再开客户端**
- **IP 和端口必须对应上**

---

## 最后总结

这套代码最核心的不是记住每个函数，而是理解这条线：

```text
服务端准备好端口等待
客户端主动连上来
客户端 send → 服务端 recv
服务端 send → 客户端 recv
```

只要记住“谁监听、谁连接、谁发送、谁接收”，socket 通信就不难。
