"""素数:一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数。比如3是素数，4不是素数"""


def sushu(num):
    if num <=1:
        return False
    for i in range(2,num):
        if num%i ==0:
            return False
    return True

def qujian(start,end):
    for i in range(start,end+1):
        if sushu(i) == True:
            print(i)
  


print(qujian(90,120))