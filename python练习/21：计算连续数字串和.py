"""求:编写一个程序，计算a+aa+aaa+aaaa+....的值，其中a是一个数字，且加数的个数由键盘确定
例如 当a=2且有5个数相加时 表达式为2+22+222+2222+22222"""
a = int(input("请输入一个数字："))
b = int(input("请输入加数的个数："))
num = 0
result = 0
for i in range(b):
     num = num * 10 + a   # 得到 2 → 22 → 222 → 2222 → ...   # 依次得到 a, aa, aaa, ...
     result = result + num
     print(num)
print(result)
