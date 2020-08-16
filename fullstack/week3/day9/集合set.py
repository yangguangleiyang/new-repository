#_author:"yangqianfeng"
#date: 2020/8/9

#把 不同的元素 组合在一起就叫集合；   最主要的功能是去重，将一个列表去重最快捷的方式就是变成集合
# 无序 不重复
#元素必须是可哈希的

# s=set("alex")
# print(s)  #{'x', 'l', 'a', 'e'}

# li=[2,3,"alexe"]
# s1=set(li)
s1=set([2,3,"alexe",2,3,4])

print(s1)   #{'alexe', 2, 3,4}

