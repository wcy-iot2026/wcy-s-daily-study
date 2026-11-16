"""需求:定义一个函数，该函数用于根据传入的整数n返回对应的倒数序列和:若n为偶数，则计算和 1/2+1/4
1/n;若n为奇数，则计算和1/1+1/3+...+ 1/n."""
def daoshu(n):
    sum=0
    if n%2==0:
        for i in range(2,n+1,2):
            sum=sum+1/i
    else:
        for i in range(1,n+1,2):
            sum=sum+1/i
    return sum

print(daoshu(4))
print(daoshu(5))