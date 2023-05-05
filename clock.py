import time

task_time = int(input('请输入倒计时时间（分钟）：'))
start_time = time.strftime('%H:%M:%S',time.localtime()) #获取格式化当前时区时间
print('开始时间：' + start_time)

for i in range(1,task_time*60): #分钟化为秒
print('剩余时间：%i秒' %(task_time*60 - i)) #每1秒打印一次
time.sleep(1)

final_time = time.strftime('%H:%M:%S',time.localtime()) #获取结束时间
print('结束时间：' + final_time)
