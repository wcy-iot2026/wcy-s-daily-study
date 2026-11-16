"""需求:定义一个函数，该函数接收一个列表newList作为参数。函数的功能是交换该列表的第一个元素和最后一个元素，
并返回交换后的列表"""
def swap_list(newList):
    if len(newList) < 2:
        return newList
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList

print(swap_list([1, 2, 3, 4, 5]))