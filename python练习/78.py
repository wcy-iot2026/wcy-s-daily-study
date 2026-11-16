"""需求:编写一个程序，
统计指定文本文件中各个单词出现的次数，并将出现次数最多的前十个单词及其对应的次数输出"""

def read_test():
    # 打开英文文本文件，按行读取并统计每个单词出现次数
    with open(r"D:\学习\python练习\english_article.txt", "r", encoding="utf-8") as f:
        result = {}  # 用字典保存：单词 -> 出现次数
        for i in f.readlines():  # 逐行读取文件
            i = i[:-1]  # 去掉行末换行符 \n
            i = i.split(" ")  # 按空格拆成单词列表
            for j in i:
                if not j:  # 跳过空字符串（空行拆出来的结果）
                    continue
                if j not in result:
                    result[j] = 1  # 第一次出现，记为 1
                else:
                    result[j] += 1  # 已出现过，次数加 1
        return result

# 调用函数，得到全部单词的统计结果
date = read_test()
# 按出现次数从高到低排序，只取前 10 个
date = sorted(date.items(), key=lambda x: x[1], reverse=True)[:10]
print(date)