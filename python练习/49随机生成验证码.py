# 需求:编写一个程序，该程序能够根据用户指定的长度随机生成一个验证码(可包含大小写英文字母以及数字)
# 1.定义一个函数，用于生成验证码
import random
import string


def shengcheng(length):
    jihe = string.ascii_letters + string.digits
    yanzhengma = ""
    for i in range(length):
        yanzhengma += random.choice(jihe)
    return yanzhengma


length = int(input("请输入验证码长度："))
print(shengcheng(length))
