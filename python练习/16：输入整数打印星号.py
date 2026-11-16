"""需求:提示用户连续输入最多7个整数(每个数在1至50之间，包含1和50)。对于每个有效输入(即在1至50之间的数)，程序
将打印该数个数的"""
for i in range(7):
    while True:
        num=int(input("请输入一个整数："))
        if num>=1 and num<=50:
            print("*"*num)
            break
        else:
            num<1 or num>50
            print("输入的整数不在1至50之间")