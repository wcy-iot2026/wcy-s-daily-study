# 简单版学生成绩管理系统
# 定义学生类：保存姓名和成绩列表
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    # 添加一次成绩
    def add_grade(self, grade):
        self.grades.append(grade)

    # 计算这个学生的平均分；还没有成绩时返回 0
    def average_grade(self):
        if not self.grades:
            return 0
        else:
            return sum(self.grades) / len(self.grades)


# 管理多名学生
class StudentManager:
    def __init__(self):
        # 用姓名当键，学生对象当值
        self.students = {}

    # 按姓名添加学生；已存在就不再添加
    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)
        else:
            print(f"学生{name}已存在")

    # 按姓名取出学生；没有则返回 None
    def get_student(self, name):
        return self.students.get(name)

    # 给指定学生添加一次成绩
    def add_grade(self, name, grade):
        student = self.get_student(name)
        if student:
            student.add_grade(grade)
        else:
            print(f"学生{name}不存在")

    # 这里的循环会打印所有学生的平均分，传入的 name 会被循环变量盖掉
    def get_average_grade(self, name):
        for name, student in self.students.items():
            print(f"学生{name}的平均成绩为{student.average_grade():.2f}")


manner = StudentManager()
manner.add_student("张三")
manner.add_student("李四")
manner.add_student("王五")
manner.add_grade("张三", 80)
manner.add_grade("李四", 90)
manner.add_grade("王五", 70)
manner.get_average_grade("李四")
