"""需求:编写一个程序，给定一个 Unix 时间戳(例如:1620747224)请将其转换为对应的日期和时间字符串
，格式为"YYYY-MM-DD HH:MM:SS"。"""
import datetime
# Unix 时间戳：从 1970-01-01 00:00:00（UTC）到该时刻的秒数
timestamp=1620747224
# fromtimestamp：把秒数变成本地日期时间
m=datetime.datetime.fromtimestamp(timestamp)
print(m)
# strftime：按格式变成字符串。%Y 年，%m 月，%d 日，%H 时，%M 分，%S 秒
print(m.strftime("%Y/%m/%d %H:%M:%S"))