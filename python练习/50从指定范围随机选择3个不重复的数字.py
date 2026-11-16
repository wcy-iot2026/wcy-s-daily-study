# 需求:从用户指定的数字范围中，随机选出 3 个不重复的数字
import random


# start：起始数字（包含）；end：结束数字（不包含）
def suiji(start, end):
    # sample 一次取出 3 个，不会重复
    return random.sample(range(start, end), 3)


start = int(input("请输入起始数字："))
end = int(input("请输入结束数字："))
print(suiji(start, end))
