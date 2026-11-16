import time

# time()：现在距离 1970-01-01 过了多少秒
now = time.time()
print("time():", now)

# ctime()：把秒数变成可读的英文字符串
print("ctime():", time.ctime(now))

# localtime()：把秒数变成本地时间，可以取出年、月、日
t = time.localtime(now)
print("localtime():", t)
print(f"例子：{t.tm_year}年{t.tm_mon}月{t.tm_mday}日 {t.tm_hour}时{t.tm_min}分{t.tm_sec}秒")

# gmtime()：把秒数变成 UTC（世界标准时间）的结构，字段和 localtime 一样。
# 中国是东八区，所以小时通常比 localtime 少 8 小时。
g = time.gmtime(now)
print("gmtime():", g)

# asctime()：把 localtime/gmtime 得到的结构再变成英文字符串。
# 不传参数时，用的是当前本地时间。
print("asctime():", time.asctime(t))
