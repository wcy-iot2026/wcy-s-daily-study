#需求:定义一个函数，该函数接收一个字典作为参数，并返回该字典中所有值的总和。
def zidian(m):
    sum=0
    for i in m.values():
        sum+=i
    return sum

m={"a":1,"b":55,"c":3}
print(zidian(m))