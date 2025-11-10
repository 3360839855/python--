# 数据类型：
# 1. 数字类型 、字符串 列表 元组 字典 集合
""" 
 数据类型
     数字：整数 浮点数 复数


"""
test = 10      # 整数
test2 = 3.14   # 浮点数 3.14
test3 = 3 + 4j # 复数
print(type(test), type(test2), type(test3))

# 算数运算符 + - * / // 地板除法 % **
print(10 + 10)  # 加法
print(10 - 5)   # 减法   
print(10 * 5)   # 乘法
print(10 / 3)   # 除法
print(10 // 3)  # 地板除法,将小数点截取掉
print(10 % 3)   # 取模
print(2 ** 3)   # 幂运算

# 不支持++ --运算符、
# 写一个九九乘法表
""" for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i*j}", end="\t")
    print() """
# 比较运算符： '>' '<' '==' '!=' '>=' '<='
print(10 > 5)
print(10 < 5)
print(10 == 5)
print(10 != 5)
print(10 >= 5)
print(10 <= 5)
# 逻辑运算符： and or not
print(10 > 5 and 5 > 3)
print(10 > 5 or 5 < 3)
# 对运算结果取反not
print(not(10 > 5))

