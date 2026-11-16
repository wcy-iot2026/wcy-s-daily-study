#需求:编写一个程序，计算并打印出指定年指定月份的第一天是星期几以及该月份的总天数。
import calendar
year=int(input('请输入年份:'))
month=int(input('请输入月份:'))
first_day,days=calendar.monthrange(year,month)
print(f'{year}年{month}月的第一天是星期{first_day+1}')
print(f'{year}年{month}月有{days}天')