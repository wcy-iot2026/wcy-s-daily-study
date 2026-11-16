#需求:定义一个名为factorial 的函数，该函数用于计算并返回给定整数的阶乘值。

def factorial(num):
    result=1
    for i in range(1,num+1):
           result =result*i
    return result

print(factorial(8))