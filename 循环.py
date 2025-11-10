# 循环for
""" for i in 取值列表: 
取值列表：
    range(5)  从0开始到4结束，不包含5
    range(1,6) 从1开始到5结束，不包含6
    range(1,6,2) 从1开始到5结束，不包含6，步长为2
    range(5,0,-1) 从5开始到1结束，包含0，步长为-1
"""
for i in range(5):
    print(i)
#换行输出
for i in range(20,0,-5):
    print("ssh root@192.168.1.%d" % i, )
# 中断循环 break continue
#打印分隔符
print("-"*50)

# while循环
""" while 条件表达式：
        条件表达式：
        True
        False
"""
sum = 0
i= 1
while i<=100:
    sum += i
    i += 1
print("1到100的和为：", sum)
#死循环 while True:
#    print("hello world")
#时间控制
import time
s = 0
while True:
    i+=1
    print("hello world+%s",i)
    time.sleep(1)
    if i==105:
        print("循环结束")
        break
