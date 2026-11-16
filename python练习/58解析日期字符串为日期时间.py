# 需求:解析日期字符串 "Aug28202512:00AM"，并打印日期时间对象
from datetime import datetime

date_str = "Aug28202512:00AM"
# strptime(字符串, 格式)：按格式把字符串变成 datetime 对象
# %b 英文月份缩写(Aug)，%d 日，%Y 四位年
# %I 12小时制的时，%M 分，%p 上午/下午(AM/PM)
date_obj = datetime.strptime(date_str, "%b%d%Y%I:%M%p")
print(date_obj)



