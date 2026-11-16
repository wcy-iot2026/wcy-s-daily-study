"""需求:定义一个函数，
它接收两个遵循"YYYY-MM-DD"格式的日期字该函数的任务是生成一个包含从begin_date到end_date
(包括两端列表作为结果返回。
lend date.表，并将该"""
import datetime
def date_range(begin_date,end_date):
    m=datetime.datetime.strptime(begin_date,"%Y-%m-%d")
    n=datetime.datetime.strptime(end_date,"%Y-%m-%d")
    lst=[]
    a=m
    while a<=n:
        astr=a.strftime("%Y-%m-%d")
        lst.append(astr)
        a+=datetime.timedelta(days=1)
    return lst
print(date_range("2026-11-06","2026-11-22"))
