# 需求:用户输入年份和月份，打印该月的日历
import calendar

year = int(input("请输入年份:"))
month = int(input("请输入月份:"))
# calendar.month(年, 月)：返回这个月的日历文本，包含星期和每一天
print(calendar.month(year, month))