# 需求:编写一个程序，计算当前工作目录下所有文件的大小总和，并将结果以千字节(KB)为单位进行打印。
import os

result = 0  # 用来累计所有文件的总字节数
for i in os.listdir():  # 遍历当前工作目录下的所有文件/文件夹名
    if os.path.isfile(i):  # 只统计文件，跳过文件夹
        result += os.path.getsize(i)  # 把该文件大小（字节）累加到 result
print(result // 1024)  # 字节转成 KB（整除 1024）后打印
