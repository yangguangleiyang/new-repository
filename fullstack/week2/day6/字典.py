#_author:"yangqianfeng"
#date: 2020/6/22

# 字典是python中唯一的映射类型，采用键值对（key-value）的形式存储数据。python对key进行哈希函数运算，根据计算的结果
# 决定value的存储地址，所以字典是无序存储的。但是在3.6版本后，字典开始是有序的，这是新的版本特征。
# 字典的key值可以是整型，字符串，元组，但是不可以是列表，集合，字典。

#字典两大特性：无序、键唯一

# 不可变类型：整型、字符串、元组
# 可变类型：列表、字典
# 不可变数据类型：当该数据类型的对应变量值发生了改变，那么它对应的内存地址也会发生改变，对于这种数据类型，就
# 称为不可变数据类型；
# 可变数据类型：当该数据类型的对应变量值发生了改变，那么它对应的内存地址不会发生改变，那么这种就是可变数据类型；
#可变数据类型是不可以作为键的

#字典的创建
# dic = {"name":"alex","age":35,"hobby":"girl"}
#另一种创建方式
# dic2 = dict((("name","alex"),("age",35),("hobby","girl")))
# print(dic2)

#增
# dic1 = {"name":"alex"}
# # dic1["age"]=35
# # print(dic1)

#改
# dic1["name"]="yangqianfeng"  #如果有已存在的键，则会修改
# print(dic1)

# dic1 = {"name":"alex"}  #如果有已存在的键，则不会修改
# ret=dic1.setdefault("age",23)  #有返回值  此处是逗号
# print(dic1)
# print(ret)

#update
# dic = {"name":"alex","age":35,"hobby":"girl"}
# dic1 = {"name":"yanglei","job":"IT"}   #如果存在重复的键，则会更新修改
# dic.update(dic1)
# print(dic)
# print(dic1)


#查
# dic = {"name":"alex","age":35,"hobby":"girl"}
# print(dic["name"])


# print(dic.keys())#找出所有的键
#print(dic.values())  #找出所有的值
#print(dic.items())  #找出所有的键值对
# 输出是dict_keys(['name', 'age', 'hobby'])  类型
# 可以转换为
# print(list(dic.keys()))

#删
dic = {"name":"alex","age":35,"hobby":"girl"}
# del dic["name"]
# print(dic)
# dic.clear()
# print(dic)

#pop
ret = dic.pop("age")  #有返回值
print(dic)
print(ret)

#popitem  随机删除
dic.popitem()