"""需求:编写一个程序，实现数字猜谜游戏并测试反应速度。该程序会生成一个0至99间的随机数字供用户猜测，通过实时反馈引导用户直至猜中。
同时，程序会记录用户的猜测耗时，并在游戏结束时提供表现反馈。"""
import random
import time
n=random.randint(0,99)
print('猜数字游戏开始!')
start=time.time()
while True:
    try:
        guess=int(input('请输入一个数字:'))
    except ValueError:
        print('请输入一个有效的数字')
    else:
        if guess>n:
            print('猜大了')
        elif guess<n:
            print('猜小了')
        else:
            end=time.time()
            jianghe=end-start
            print(f'恭喜你，猜对了!你用了{jianghe:.2f}秒')
            break


