"""需求:从 students_grade_file.txt 文件中读取学生的成绩数据
，并计镀这些成结中的最高分、最低分以及平的分(平均分需保留两位小析)"""
def read_student():
    with open("D:\学习\python练习\students_grade_file.txt", "r", encoding="utf-8") as f:
        result=[]
        for i in f.readlines():
            i=i[:-1]
            i=i.split(",")
            result.append(int(i[-1]))
        print(result)
    max_score=max(result)
    min_score=min(result)
    average_score=sum(result)/len(result)
    return max_score,min_score,average_score

    
date=read_student()
print(f"最高分：{date[0]}，最低分：{date[1]}，平均分：{date[2]:.2f}")