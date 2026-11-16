#需求:定义一个函数，该函数接收年份、月份和日期作为参数，计算这一天是该年的第几天
def runnian(year):        
    return year%4==0 and year%100!=0 or year%400==0

def day(years,month,day):
    m=[31,28,31,30,31,30,31,31,30,31,30,31]
    if runnian(years):
        m[1]=29
    result=sum(m[:month-1])+day  #这一行牢记
    return result

print(day(2024,12,31))
   