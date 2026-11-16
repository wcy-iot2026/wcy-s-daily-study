# 需求:把表示时间的字符串转换成以秒为单位的时间戳
import time

shijian = "2026-11-05 10:00:00"
# strptime(字符串, 格式)：按格式把字符串解析成时间结构，结果和 localtime() 一样。
# %Y 四位年，%m 月，%d 日，%H 时（24小时），%M 分，%S 秒。
m = time.strptime(shijian, "%Y-%m-%d %H:%M:%S")
print(m)
# mktime(时间结构)：把本地时间结构转成秒数（时间戳），和 time() 的单位相同。
n = time.mktime(m)
print(n)

shijian = "2026/11/05 10:00:00"
# 字符串里的分隔符变了，格式字符串也要改成同样的符号。
m = time.strptime(shijian, "%Y/%m/%d %H:%M:%S")
n = time.mktime(m)
print(n)

# strftime(格式, 时间结构)：strptime 的反方向，把时间结构再变成字符串。
print(time.strftime("%Y年%m月%d日 %H:%M:%S", m))
