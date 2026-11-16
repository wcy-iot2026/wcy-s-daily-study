"""需求:定义一个函数，该函数接收一个人的年龄作为参数。
如果年龄不在合法范围内(比如小于0或大于120)，则抛出异常。"""
def yanzhengnianling(nianling):
    if nianling<0 or nianling>120:
        raise ValueError("请输入正确的年龄")
    return nianling

try:
    print(yanzhengnianling(888))
except ValueError as e:
    print(e)