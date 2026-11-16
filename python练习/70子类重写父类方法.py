"""需求:
1.定义一个父类Vehicle，包含一个方法describe，用于描述车辆的基本信息。
2.定义一个子类Car，继承自Vehicle，并重写describe方法，以提供关于汽车的特定信息。"""
class fulei():
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def describe(self):
        return f"This is a {self.make} {self.model}"
m=fulei('Toyota','Camry')
print(m.describe())
class zilei(fulei):
    def __init__(self,year,make,model):
        super().__init__(make,model)
        self.year=year
    def describe(self):
        return f"This is a {self.make} {self.model} {self.year}"
car=zilei(2024,'Toyota','Camry')
print(car.describe())
