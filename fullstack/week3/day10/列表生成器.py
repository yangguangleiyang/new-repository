#_author:"yangqianfeng"
#date: 2020/8/23

#列表生成式
# a=[x*2 for x in range(10)]  #列表生成式格式
# print(a)

# def f(n):
#     return n*n
# a=[f(x) for x in range(10)]
# print(a)

#列表生成器
# s=(x*2 for x in range(10))
# print(s)  #<generator object <genexpr> at 0x0000020C6D9A1C80>  #相当于一个厨师十道菜还没做好，想吃哪个立马做哪个

        # print(next(s))   #等价于s._next_()  输出0
        # print(next(s))   #输出2
        # print(next(s))   #输出4

#生成器就是一个可迭代对象

# for i in s:    #用此方法 上面的方法太占内存
#     print(i)

#第二种方法生成 生成器

def foo():
    print("ok1")
    yield 1

    print("ok2")
    yield 2

# for i in foo():
#     print(i)
#执行结果 OK1  1  ok2  2

g=foo()
next(g) #执行结果 ok1   记住 不是ok1 1
next(g)
