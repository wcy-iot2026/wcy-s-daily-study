"""
求:编写一个程序，搜索指定目录(含其子目录)内的所有.txt文件，并找出其中最大的文件及其大小"""
import os

dir_path = r"D:\学习\python练习"  # 要搜索的根目录
result = []  # 存放 (文件路径, 大小KB) 的列表

# os.walk 会递归遍历目录及其子目录
# root: 当前文件夹路径；dirs: 子文件夹列表；files: 当前文件夹下的文件名列表
for root, dirs, files in os.walk(dir_path):
    for file in files:  # 逐个检查当前目录下的文件
        if file.endswith(".txt"):  # 只处理 .txt 文件
            m = os.path.join(root, file)  # 拼出文件的完整路径
            n = os.path.getsize(m) // 1024  # 获取文件大小，并转换成 KB
            result.append((m, n))  # 把路径和大小一起存进列表

# 按文件大小从大到小排序
result = sorted(result, key=lambda x: x[1], reverse=True)
print(result[0])  # 打印最大的那个 .txt 文件及其大小
