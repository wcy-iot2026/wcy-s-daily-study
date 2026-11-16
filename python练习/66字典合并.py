import copy

# 合并两个字典，返回新字典，不改原来的 dict1
def hanshu(dict1, dict2):
    # copy.copy：复制一份 dict1，后面修改不会影响原字典
    dict3 = copy.copy(dict1)
    # update：把 dict2 的键值放进来；同名键用 dict2 的值覆盖
    dict3.update(dict2)
    return dict3

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
# 'b' 两边都有，结果里的 'b' 是 3
print(hanshu(dict1, dict2))
