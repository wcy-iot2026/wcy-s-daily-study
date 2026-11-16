#需求:定义一个函数，该函数用于统计指定元素在指定列表中出现的次数。
def count_element(newList,element):
    count = 0
    for i in newList:
        if i == element:
            count += 1
    return count

print(count_element([1, 2, 3, 4, 5],3)) 