#需求:编写一个程序，实现简单秒表功能。该程序在用户按下回车键后开始计时，\
# 在用户中断程序时停止计时
import time
input('按下回车键开始计时:')
start=time.time()
print('计时开始')
try:
    while True:
        end=time.time()
        jianghe=end-start
        #使用格式化字符串来限制小数点后的位数，并覆盖上次输出
        print(f'\r总共耗时:{jianghe:.2f}秒',end='') 
        time.sleep(1)
except KeyboardInterrupt:
    end=time.time()
    jianghe=end-start
    print(f'\n总共耗时:{jianghe:.2f}秒') 

