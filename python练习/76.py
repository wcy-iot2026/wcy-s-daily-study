# 需求:从 students_grade_file.txt 读取学生数据(学号、姓名、成绩)，并按成绩排序
def read_student():
    with open(r"D:\学习\python练习\666\666", "r", encoding="utf-8") as f:
        result=[]
        for i in f.readlines():
            i=i[:-1]
            i=i.split(',')
            result.append(i)
        return result
def sort_student(date):
    date.sort(key=lambda x: int(x[2]),reverse=True)
    return date
def weite_student(date):
    with open(r"D:\学习\python练习\666\666", "w", encoding="utf-8") as f:
        for i in date:
            f.write(','.join(i)+'\n')

date=read_student()
print(date)
date=sort_student(date)
print(date)
