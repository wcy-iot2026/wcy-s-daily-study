#需求:编写一个程序，该程序将遍历并打印从0到2999的所有整数，同时计算并输出整个遍历过程所消耗的总时间。
import time
start=time.time()
for i in range(3000):
    print(i)
end=time.time()
print(f"遍历打印0-2999耗时：{end-start}秒")