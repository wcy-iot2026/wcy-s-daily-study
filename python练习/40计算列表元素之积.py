#需求:定义一个函数，该函数接收一个整数列表作为参数，并返回列表中所有元素的乘积。
def multiply_list(newList):
    result = 1
    for i in newList:
        result *= i
    return result

print(multiply_list([1, 2, 3, 4, 5]))