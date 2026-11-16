#需求:定义一个函数，该函数用于计算并返回给定数字列表中所有数字的总和。
def he(list):
    sum = 0
    for i in list:
        sum+=i
    return sum

print(he([1,2,3,4,5]))
