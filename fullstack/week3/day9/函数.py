#_author:"yangqianfeng"
#date: 2020/8/9

# def f(x,y):
#     print(x+y)
# f(3,5)

# def add(*args):   # *args 为不定长参数 可接受很多参数
#     print(args)
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
# add(1,2,4)

# def area(width,height):
#     print(width*height)
# area(4,5)

#

# def printinfo(arg1,*vartuple):
#     print("输出：")
#     print(arg1)
#     print(vartuple)
#     return
# printinfo(30,70,60,50)

# def f2(**kwargs):
#     print(kwargs)
# f2(name="yang",age=28,hobby="girl")    #输出为字典{'name': 'yang', 'age': 28, 'hobby': 'girl'}


#高阶函数
# def f(n):
#     return n*n
#
# def foo(a,b,func):
#     return func(a)+func(b)
#
# s=foo(2,3,f)
# print(s)

# for i in range(5):
#     print(i)
#递归函数  用函数写出阶乘  5*4*3*2*1
# def f(n):
#     sum=1
#     for i in range(n):
#         sum=sum*(i+1)
#     return sum
# print(f(5))

#递归写法：
# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

def peibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return peibo(n-1)+peibo(n-2)
print(peibo(8))