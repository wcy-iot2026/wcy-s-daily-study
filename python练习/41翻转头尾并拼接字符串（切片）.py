"""需求:定义一个函数，该函数接收一个字符串和一个整数作为参数。完成以下操作:
1.从字符串头部截取指定数量的字符并翻转。
2.从字符串尾部截取相同数量的字符并翻转。
3.分别打印出头部和尾部翻转后与剩余部分拼接后的新字符串。"""
def pinjie(zifuchuan,n):
    num1 = zifuchuan[:n][::-1]
    num2=zifuchuan[n:]
    print(num1+num2)

    num3=zifuchuan[-n:][::-1]
    num4=zifuchuan[:-n]
    print(num4+num3)
pinjie("1234567890",3)
