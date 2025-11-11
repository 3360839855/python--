# 列表的定义： 定义在一对[]中的数据，类似于数组 支持在列表中存储任何类型的数据
# 列表是可变数据类型，还有字典也是可变数据类型
my_list = [1, 2, 3, 'hello', 4.5, True]
for i in my_list:
    #取消换行，并且俩个输出之间加个空格区别，每次循环之间换行
    print(i, end=" ")
    print(type(i), end=" ")
    print()
print("")

# 列表解析，快速生成列表，生成数据，在列表中添加一个循环，让其自动生成数据
my_list = [i for i in range(10)]
print(my_list)
my_list = [i for i in range(10) if i % 2 == 0]
print(my_list)
#----------------列表的操作符----------------
# 列表的拼接
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

# 列表的复制
list4 = list1.copy()
print(list4)

#列表长度 len()
print(len(list3))

#成员包含关系in not in
list5 = [[1,2], [3,4], [5,6]]
print(1 in list5)
print(4 not in list5)

# 列表的索引和切片
print(list1[0])
print(list1[1:3])
list1[0] = 100
print(list1[0])

# ----------------列表的方法----------------
# append() 添加元素到列表末尾
list1.append(7)
print(list1)
list1.append([8,9])
print(list1)

# ----------列表的遍历----------
apps = ['QQ', '微信', '支付宝', '抖音']
for app in apps:
    print(app)
for i in range(len(apps)):
    print(apps[i])

# 遍历字符串
for char in "hello":
    print(char)


#  ssh 用户名@ip -p 端口号
servers = [["10.1.1.1","admin",22], ["10.1.1.2","root",22], ["10.1.1.3","user",22]]
for i,j ,k  in servers:
    print("ssh %s@%s -p %s" % (j,i,k))

