#需求:定义一个学生类，用于存储学生的基本信息(如姓名、年龄、学号)，并提供查询这些信息的方法。
class Student:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id

    def getname(self):
        return self.name

    def getage(self):
        return self.age

    def getid(self):
        return self.id

student=Student('张三',20,123456)
print(student.getname())
print(student.getage())
print(student.getid())