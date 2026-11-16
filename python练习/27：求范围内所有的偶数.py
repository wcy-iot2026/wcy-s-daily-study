#需求:定义一个函数，该函数用于返回指定范围内所有偶数的列表。
list = []
def hanshu(start,end):
    for i in range(start,end+1):
        if i%2==0:
            list.append(i)
    return list

print(hanshu(1,10))