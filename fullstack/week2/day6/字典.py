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
#dic = {"name":"alex","age":35,"hobby":"girl"}
#另一种创建方式
# dic2 = dict((("name","alex"),("age",35),("hobby","girl")))
# print(dic2)

#增
# dic1 = {"name":"alex"}
# dic1["age"]=35
# print(dic1)

#改
#dic["name"]="yangqianfeng"  #如果有已存在的键，则会修改
# print(dic1)

#dic = {"name":"alex"}  #如果有已存在的键，则不会修改
# ret=dic1.setdefault("age",23)  #有返回值  此处是逗号
#print(dic)
# print(ret)

#update
# dic = {"name":"alex","age":35,"hobby":"girl"}
# dic1 = {"name":"yanglei","job":"IT"}   #如果存在重复的键，则会更新修改
# dic.update(dic1)
# print(dic)
# print(dic1)


#查
#dic = {"name":"alex","age":35,"hobby":"girl"}
#print(dic["name"])

#print(dic)
# print(dic.keys())#找出所有的键   #dict_keys(['name', 'age', 'hobby'])
# print(dic.values())  #找出所有的值   #dict_values(['alex', 35, 'girl'])
#print(dic.items())  #找出所有的键值对  #dict_items([('name', 'alex'), ('age', 35), ('hobby', 'girl')])
# 输出是dict_keys(['name', 'age', 'hobby'])  类型
# 可以转换为
#print(list(dic.items()))

#删
# dic = {"name":"alex","age":35,"hobby":"girl"}
# del dic["name"]
# print(dic)
# dic.clear()
# print(dic)

#pop
'''ret = dic.pop("age")  #有返回值
print(dic)
print(ret)'''

#popitem  随机删除
# dic.popitem()

#其他操作及方法   fromkeys
# dic6 = dict.fromkeys(["host1","host2","host3"],"test")
# print(dic6) #{'host1': 'test', 'host2': 'test', 'host3': 'test'}



#字典的嵌套

#排序
# dic = {5:"555",6:"666",7:"777"}
# print(sorted(dic))    #[5, 6, 7]  等同于print(sorted(dic.keys()))  根据键
# print(sorted(dic.values()))   #['555', '666', '777']   根据值
# print(sorted(dic.items()))   #[(5, '555'), (6, '666'), (7, '777')]   根据键


#字典的遍历
#循环遍历键
dic = {"name":"alex","age":35,"hobby":"girl"}
for i in dic:
    #print(i)
    print(i,dic[i])   #这样键和值就都打印出来了
for i,v in dic.items():
    print(i,v)


#字符串
#String 操作

#重复输出字符串
#print("hello"*5)

#通过索引获取字符串中字符，和列表中的切片操作是相同的
#print("hellowordhelloword"[3:-1])

#判断元素是否在列表中，返回True和False
# print("el"in"hello")

#字符串拼接
# a = "123"
# b = "abc"
# c =a+b
# print(c)   #占内存 不建议

#或者
# c = "".join([a,b])
# print(c)




