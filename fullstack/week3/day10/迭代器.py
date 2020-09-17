#生成器都是迭代器，迭代器不一定是生成器
l=[1,3,5,7]
g=iter(l)
print(g)  #<list_iterator object at 0x000001FDEAE7D430>

#什么是迭代器？
#满足两个条件：1.有iter方法  2.有next方法
print(next(g))
print(next(g))

#for 循环内部三件事
#1.调用可迭代对象的iter方法返回一个迭代器对象
#2.不断调用迭代器对象的next方法
#3.处理stop异常
for i in [1,2,3,4]:
    print(i)
