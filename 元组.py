# 元组的定义： 定义在一对圆括号中的数据，元素之间用逗号分隔
# 元组的不可变性： 元组一旦定义，其元素不能被修改、添加或删除
t = (1, 2, 3, 4, 5)
for i in t:
    print(i)
test_01 = ([1, 2], [3, 4], [5, 6])
for i in test_01:
    i[0] += 10
print(test_01)

# 单元数组
# 在元组中定义一个字符串的时候一定要跟一个,不然就会被识别成字符串，而不是元组
single_tuple = ('hello',)
test_02 = ('hello')
print(type(single_tuple))
print(type(test_02))
