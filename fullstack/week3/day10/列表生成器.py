#_author:"yangqianfeng"
#date: 2020/8/23

#列表生成式
# a=[x*2 for x in range(10)]  #列表生成式格式
# print(a)

# def f(n):
#     return n*n
# a=[f(x) for x in range(10)]
# print(a)

#生成器
# s=(x*2 for x in range(10))
# print(s)  #<generator object <genexpr> at 0x0000020C6D9A1C80>  #相当于一个厨师十道菜还没做好，
# 想吃哪个立马做哪个

        # print(next(s))   #等价于s._next_()  输出0
        # print(next(s))   #输出2
        # print(next(s))   #输出4

#生成器就是一个可迭代对象

# for i in s:    #用此方法      #上面的方法太占内存
#     print(i)

#第二种方法生成 生成器

# def foo():
#     print("ok1")
#     yield 1
#
#     print("ok2")
#     yield 2

# for i in foo():
#     print(i)
#执行结果 OK1  1  ok2  2

# g=foo()
# next(g) #执行结果 ok1   记住 不是ok1 1    yield 相当于return 没有显示1  是因为for循环里打印了1  next
#方法里没有打印1
# next(g)

#什么是可迭代对象   对象拥有 iter方法的

#实现裴波那契数列
# def fib(max):
#     n,b,a=0,0,1
#     while n<max:
#         #print(a)
#         yield b
#         b,a=a,a+b
#         n=n+1
# fib(8)
#print(g)  #<generator object fib at 0x00000216680B02E0>
    # print(next(g))
    # print(next(g))
    # print(next(g))
# for i in fib(8):
#     print(i)

#send方法的使用
# def bar():
#     print("ok1")
#     count=yield 1
#     print(count)
#     yield 2
#
# b=bar()
# b.send(None)  #send的目的是可以传参数给yield ,但是第一次是不能传参的，只能传None，这段话相当于next(b)
# b.send("eeee")


#吃包子实例
import time

def consumer(name):
    print("%s准备吃包子啦"%name)
    while True:
        baozi=yield
        print("包子%s来了，被%s吃了"%(baozi,name))

def producer(name):
    C=consumer("A")
    c2=consumer("B")
    C.__next__()
    c2.__next__()
    print("我开始做包子了")
    for i in range(10):
        time.sleep(1)
        print("做了两个包子")
        C.send(i)
        c2.send(i)
producer("alex")