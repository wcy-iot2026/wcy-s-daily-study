import datetime

# now()：取得当前的本地日期和时间
n = datetime.datetime.now()
print(n)

# strftime(格式)：把日期时间按指定格式变成字符串
# %Y 四位年，%m 月，%d 日，%H 时，%M 分，%S 秒
m = n.strftime("%Y/%m/%d %H:%M:%S")
print(m)

# 这些是 n 里的属性，直接取出年、月、日、时、分、秒、微秒
print("年", n.year)
print("月", n.month)
print("日", n.day)
print("时", n.hour)
print("分", n.minute)
print("秒", n.second)
print("微秒", n.microsecond)



