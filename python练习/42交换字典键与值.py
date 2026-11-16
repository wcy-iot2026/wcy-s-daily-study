#需求:定义一个函数，用于交换指定字典的 key 和 value。
def jiaohuan(dict1):
    dict2={}
    for key in dict1:
        dict2[dict1[key]]=key
    return dict2

original={'a':3,'b':2}
print(jiaohuan(original))
