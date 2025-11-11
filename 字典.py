# 字典的定义： 定义在一对{}中的数据，类似于map，支持通过键值对存储数据
# key:value key必须是唯一，value可以任意类型的值或者重复
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key in my_dict:
    print(key, my_dict[key])
print("")

# 字典的操作
# 添加/修改元素
my_dict['age'] = 26
my_dict['gender'] = 'female'
my_dict['code'] = "18.25"
print(my_dict)

# 删除元素
del my_dict['city']
print(my_dict)

# 字典的遍历
for key, value in my_dict.items():
    print(key, value)

print(my_dict['name'])

version = my_dict.get("name")
print(version)

# 字典对象的操作方法
print(my_dict.keys())    # 获取所有键
print(my_dict.values())  # 获取所有值
print(my_dict.items())   # 获取所有键值对
# my_dict.clear()          # 清空字典
print(my_dict)


# 遍历字典的键值对
for key, value in my_dict.items():
    print(key, value)

