""" 
逻辑条件判断
1. if 条件表达式：满足条件执行代码块
2. if 条件表达式：满足条件执行代码块 else: 不满足条件执行代码块
3. if 条件表达式：满足条件执行代码块 elif 其他条件表达式
    else: 不满足条件执行代码块
    4. if 条件表达式：满足条件执行代码块 elif 其他条件表达式
    elif 其他条件表达式
    else: 不满足条件执行代码块
 """
# num = int(input("请输入一个数字："))
if num > 0:
    print("输入的数字是正数")
elif num == 0:
    print("输入的数字是零")
else:
    print("输入的数字是负数")
#d打印一个分割线
print("-"*50)
# python通过缩进来区分代码块
num = int(input("请输入一个数字："))
if num > 0:
    print("输入的数字是正数")
    if num > 10:
        print("输入的数字大于10")
    else:
        print("输入的数字小于10")
else:
    print("输入的数字是负数")