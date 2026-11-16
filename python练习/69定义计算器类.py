#需求:定义一个简单的计算器类，这个类支持加、减、乘、除四种基本运算。
class jisuanqi:
    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        if b==0:
            return '除数不能为0'
        else:
            return a/b
jisuanqi=jisuanqi()
print(jisuanqi.add(1,2))    
print(jisuanqi.sub(1,2))    
print(jisuanqi.mul(1,2))
print(jisuanqi.div(1,2))

