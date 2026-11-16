#需求:定义一个函数，该函数用于尝试将用户输入的字符申转换为整数。如果转换成功，则返回整数。如果转换失败，则返回错误信
def zhuanhuan(zifuchuan):
    try:
        num=int(zifuchuan)
    except:
      return "输入错误,请输入整数"  
    return num
print(zhuanhuan("12ff"))
