#浅拷贝
a=[2,4,"alex",[5,6,89]]
# b=a.copy()
# print(b)  #此时b和a都指向了同一内存地址
#
# a.append("xiaowang")  #新开辟了一块内存“xiaowang” 指向a，但是并没有指向b
# print(a)
# print(b)
#
# a[3][1]="lisi"  #修改a中列表的值  同时b指向的是列表，所以其中的值改变了，b也会改变
# print(a)
# print(b)

#深拷贝
# 深拷贝完全赋值被复制对象的元素，不是复制内存地址，是开辟新的内存空间将被复制对象的值放在了新的内存空降中，
# 并将新的内存地址指向了新的变量，这样的话，修改原对象不会对新的对象产生影响。
#
# 深拷贝是在另一块地址中创建一个新的变量，同时容器内的元素的地址也是新开辟的，仅仅是值相同而已，是完全的副本。

import copy
c=copy.deepcopy(a)
print(c)
a.append("qianfengzhijia")
c[0]="one"
print(a)
print(c)