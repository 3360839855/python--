#字符串定义： 定义在一对引号中的数据
#原始字符串定义： 避免特殊字符转义 r"字符串内容"
win_file_name = r"C:\new\test.py"
print(win_file_name)

#单引号定义字符串
str_01 = 'hello world'
print(str_01)

#双引号定义字符串----单引号和字符串和双引号字符串无区别
str_02 = "hello world"
print(str_02)

#字符串的拼接
str_03 = str_01 + " " + str_02
print(str_03)

#字符串的重复
print("----" * 5)

#字符串的长度len()
print(len(str_03))

#判断字符串的包含关系，in not in
print("el" in "hello world")
print("eo" not in "hello world")

#字符串的索引和切片 字符串[起始:结束:步长]
str_04 = "abcdefghij"
print(str_04[0])   # 输出第一个字符
print(str_04[-1])  # 输出最后一个字符
print(str_04[1:5]) # 输出第二到第五个字符

#字符串倒置
print(str_04[::-1])  # 输出倒置的字符串

#字符串对象的操作方法
test_str = "  Hello World  "
print(test_str.upper())    # 转大写
print(test_str.lower())    # 转小写
print(test_str.strip())    # 去除首尾空格

#分割字符串，取第二列元素
print(test_str.strip().split(" ")[1])  # 按空格分割字符串并取第二个元素

#在python中，类型是弱类型的，变量不需要声明类型，变量在赋值时会自动根据赋值内容确定变量类型

#判断字符串的组成结构，is开头的方法
print("12345".isdecimal())  # 是否全是数字组成
print("ansdb123".isnumeric())  # 是否全是数字组成

#字符串替换replace()
print("Hello World".replace("Hello", "Hi"))  # 将Hello替换为Hi

che = input("请输入：Y/N").upper().split(" ")
if che == "Y":
    print("你选择了是")
elif che == "N":
    print("你选择了否")
else:
    print("无效输入")

