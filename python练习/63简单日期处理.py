"""需求:编写一个程序，使用 datetime 模块完成以下任务:
1.输出今日日期(YYYY-MM-DD 格式)。
2.创建并输出宫崎骏生日(1941年1月5日)的日期。
3.计算并输出宫崎骏生日的下一天。
4.计算并输出宫·崎骏的一岁生日日期。"""
import datetime
# date.today()：今天的日期，格式是 YYYY-MM-DD
today=datetime.date.today()
print(today)
# date(年, 月, 日)：创建 1941年1月5日
birthday=datetime.date(1941,1,5)
print(birthday)
# timedelta(days=1)：1 天，加到生日上就是下一天
next_day=birthday+datetime.timedelta(days=1)
print(next_day)
# timedelta(days=365)：365 天，大约是一岁生日
one_year_old=birthday+datetime.timedelta(days=365)
print(one_year_old)