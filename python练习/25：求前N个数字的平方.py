"""需求:定义一个函数，该函数用于计算从1**2到N**2的所有整数的平方和"""
def pingfang(n):
    sum = 0
    m=0
    for i in range(1,n+1):
        m=i**2
        sum+=m
    return sum

print(pingfang(10))

