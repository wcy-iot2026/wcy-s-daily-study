"""需求:定义一个函数，该函数接收一个正整数参数roWs，
其功能是打印出一个由星号*构成的、具有roWS指定行数的菱形图案。"""

def print_diamond(rows):
    if rows % 2 == 0:
        print("请输入奇数")
        return
    for i in range(1,rows,2):
        kongge =  " "*((rows -i)//2)
        xinghao = "*"*i
        print(kongge + xinghao)

    for i in range(rows,0,-2):
        kongge = " "*((rows -i)//2)
        xinghao = "*"*i
        print(kongge + xinghao)
print_diamond(5)