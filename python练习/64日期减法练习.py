import datetime

# riqi：日期字符串，格式是 年/月/日；day：要减去的天数
def date_sub(riqi, day):
    # strptime：把字符串变成日期时间
    n = datetime.datetime.strptime(riqi, "%Y/%m/%d")
    # timedelta(days=day)：表示 day 天
    m = datetime.timedelta(days=day)
    # 日期减去这段时间
    jieguo = n - m
    # strftime：再变回 年/月/日 字符串
    return jieguo.strftime("%Y/%m/%d")

# 2026/11/06 减去 10 天
print(date_sub("2026/11/06", 10))
