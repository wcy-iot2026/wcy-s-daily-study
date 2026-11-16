"""斐波那契数列:数列的前两项均为1，从第三项开始，每一项都是其前两项的和。
如:1、1、2、3、5、8、13,21、34."""
def feibonaqishulie(n):
    if n<1:
        return 0
    if n==1 or n==2:
        return 1
    else:
        return feibonaqishulie(n-1)+feibonaqishulie(n-2)

print(feibonaqishulie(10))