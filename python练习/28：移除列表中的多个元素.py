#需求:定义一个函数，该函数用于从第一个列表 list1中移除所有存在于第二个列表List2中的元素。
def yichu(list1,list2):
    for i in list2:
        if i in list1:
            list1.remove(i)
    return list1
print(yichu([1,2,3,4,5],[2,4]))