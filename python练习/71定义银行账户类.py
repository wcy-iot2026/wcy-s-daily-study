#需求:定义一个简单的银行账户类，这个类支持存款和取款操作。
class bankaccount:
    def __init__(self,zijin):
        self.zijin=zijin

    def cunkuan(self,account):
        if account>0:
            self.zijin+=account
        else:
            print('存款金额不能小于0')

    def qukuan(self,account) :
        if account>0 and account<=self.zijin:
            self.zijin-=account
        else:
            print('取款金额不能小于0或大于账户余额')

    def getzijin(self):
        return self.zijin

account=bankaccount(1000)
account.cunkuan(500)
account.qukuan(200)
print(account.getzijin())   