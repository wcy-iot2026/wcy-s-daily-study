#需求:定义一个函数，该函数用于对列表进行去重处理，并返回一个新的列表，其中不包含任何重复的元素。
def quchong(list):
    for i in list:
        if i in list:
            list.remove(i)
    return list

print(quchong([1,2,3,4,5,1,2,3,4,5]))