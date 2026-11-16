nums = input("请输入多个数字，用空格隔开：").split()
num=[]
for i in nums:
    i = int(i)
    num.append(i)
num.sort()
print(num)