#需求:编写一个程序，用于遍历指定目录下的所有文件，并根据每个文件的后缀名进行分类。
import os
import shutil  # 用于移动文件

dir_path = r"D:\学习\python练习"  # 要整理的目录
for i in os.listdir(dir_path):  # 遍历目录下的所有文件/文件夹名
    m = (os.path.splitext(i)[1])  # 取出后缀名，如 ".py"
    m = m[1:]  # 去掉点，得到 "py"
    # 如果还没有以该后缀命名的文件夹，就创建一个
    if not os.path.isdir(f"{dir_path}\{m}"):
        os.mkdir(f"{dir_path}\{m}")
    start = (f"{dir_path}\{i}")  # 原文件路径
    end = (f"{dir_path}\{m}\{i}")  # 移动后的目标路径（后缀文件夹里）
    shutil.move(start, end)  # 把文件移动到对应后缀文件夹
