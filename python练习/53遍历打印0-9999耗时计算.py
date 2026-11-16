"""需求:编写一个程序，计算遍历从0 到 9999所有整数所需的时间，
并将这个时间差以保留三位小数的浮点数形式输出。"""
import time
start=time.perf_counter()
for i in range(9000):
    print(i)
end=time.perf_counter()
print(f"遍历打印0-9999耗时：{end-start:.3f}秒")