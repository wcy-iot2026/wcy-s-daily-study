# 需求:计算两个日期之间相差多少天
import datetime

birthday = "2000-01-01"
# now()：当前日期时间
m = datetime.datetime.now()
# strptime：把字符串按 %Y-%m-%d（年-月-日）变成日期时间
f = datetime.datetime.strptime(birthday, "%Y-%m-%d")
# 两个日期相减，得到时间差 d
d = m - f
# d.days：相差的整天数，类型是整数
print(d.days, type(d.days))
# 再除以 365，大约是相差多少年
print(d / 365)