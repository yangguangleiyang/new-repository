#_author:"yangqianfeng"
#date: 2020/8/9

#把 不同的元素 组合在一起就叫集合；   最主要的功能是去重，将一个列表去重最快捷的方式就是变成集合
# 无序 不重复
#元素必须是可哈希的,即不可变的数据结构(字符串str、元组tuple、对象集objects)。
#不可哈希的数据类型，即可变的数据结构 (字典dict，列表list，集合set)

# s=set("alex")
# print(s)  #{'x', 'l', 'a', 'e'}

# li=[2,3,"alexe",2,34,5,3]
# s1=set(li)
s1=set([2,3,"alexe",2,3,4])
# print(s1)   #{2, 3, 34, 5, 'alexe'}
# slist=list(s1)   #将集合转换为列表
# print(slist)    #[2, 3, 34, 5, 'alexe']

#两个集合之间的运算
# a=set("ABCDE")
# b=set("CDEFG")
# print(a-b)  #a-b  集合a中包含而集合b中不包含的   {'A', 'B'}
# print(a|b)   #集合a和集合b中包含的所有元素
# print(a&b)   #集合a和集合b中共同包含的元素
# print(a^b)   #集合a和集合b中不同时包含的元素

#添加元素
# li=[2,3,"alexe",2,34,5,3]
# s=set(li)
# print(s)
# s.add("wuchao")   #用add添加的话,添加的是整体"wuchao"
# print(s)
# s.update("jinxin")   #用update添加的话，添加的是"j" "i" n x i n
# print(s)

#移除元素   但是元素不存在的话，会报错
# s=set([2,3,"alexe",2,34,5,3])
# s.remove(34)
# print(s)
#
# s.pop()   #随机删除集合里的一个元素
# print(s)

print(s1)   #{'alexe', 2, 3,4}
#计算元素中个数
# s=set([2,3,"alexe",2,34,5,3])
# print(len(s))
#清空集合
# s.clear()
# print(s)

#判断元素是否在集合内
#print("alexe"in s)

