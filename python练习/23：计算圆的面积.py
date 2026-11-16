"""需求:定义一个函数，该函数用于计算并返回给定半径的圆的面积(要求结果保留两位小数)。"""
def mianji(r):
    result = 3.14 * r * r
    #保留两位小数   round(浮点数，保留几位)
    result = round(result, 2)
    return result


print(f"半径为5的圆的面积为{mianji(5)}")