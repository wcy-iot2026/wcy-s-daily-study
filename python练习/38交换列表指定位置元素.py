#需求:定义一个函数，该函数用于将指定列表中指定索引位置的两个元素对调。
def swap_list(newList,index1,index2):
    if index1 < 0 or index2 < 0 or index1 >= len(newList) or index2 >= len(newList):
        return "索引越界"
    newList[index1], newList[index2] = newList[index2], newList[index1]
    return newList
  
print(swap_list([1, 2, 3, 4, 5],1,4))       