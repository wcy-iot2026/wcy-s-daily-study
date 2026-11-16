"""需求:用户输入一个整数，判断它是奇数还是偶数。"""
num = int(input("请输入一个整数："))
if num % 2 == 0:
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")
