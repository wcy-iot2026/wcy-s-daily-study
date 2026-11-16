"""持续提示用户输入一个数字，并对该数字进行平方运算。如果平方运算结果小于 50，则停止输入。"""
while True:
    num = int(input("请输入一个数字："))
    result = num ** 2
    print(f"{num}的平方是{result}")
    if result < 50:
        break
