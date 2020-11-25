#特殊方法一
# class Foo:
#     def __init__(self):
#         print("init")
#     def __call__(self, *args, **kwargs):
#         print("call")
# obj=Foo()
# obj()     #对象后面加个括号，默认执行call，（规定）

#Foo()()   也可以这么写

#特殊方法二
# class Foo:
#     def __init__(self):
#         pass
#     def __int__(self):
#         return 111
#     def __str__(self):
#         return "alex"
#
# obj=Foo()
# print(obj,type(obj))
#
# #int 对象，自动执行对象的__int__方法，并将返回值赋值给int对象
# r=int(obj)
# print(r)
#
# i=str(obj)
# print(i)


# class Foo:
#     def __init__(self,n,a):
#         self.name=ne
#         self.age=a
#     def __str__(self):
#         return self.name
# obj=Foo('alex',18)
# print(obj)  #print默认调用了str方法，相当于print(str(obj))

#类的特殊方法三

# class Foo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.n=123
# obj=Foo("yang",18)
# d=obj.__dict__       #__dict__的作用是将封装里的内容以字典的形式展现出来
# print(d)

#类的特殊方法四
# class Foo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __getitem__(self, item):
#         return item+10
#     def __setitem__(self, key, value):
#         print(key,value)
#     def __delitem__(self, key):
#         print(key)
#
# li=Foo("yang",18)
# r=li[8]
# print(r)
#
# li[100]="alex"

# del li[900]

#类的特殊方法五
class Foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __iter__(self):
        return iter([11,22,33])

li=Foo("yang",18)
#如果类中有__iner__方法，对象是可迭代对象
#对象.__iter__()返回值：迭代器
#for循环遇到的是迭代器，next
#for循环遇到是的是可迭代对象，对象.__iter__(),迭代器，next
#1.执行for i in li时，默认获取li对象的类中的__iter__方法，并获取其返回值
#2.循环上一步中返回的对象
for i in li:
    print(i)

#类的特殊方法六
class Foo:
    pass
obj=Foo()
#obj是Foo的对象
#Foo类也是一个对象，是type的对象
#类都是type类的对象

class MyType(type):
    def __init__(self,*args,**kwargs):
        print(123)
        pass
    def __call__(self, *args, **kwargs):
        self.__new__()

class Foo(object,metaclass=MyType):
    def __init__(self):
        pass
    def __new__(cls, *args, **kwargs):
        pass
    def func(self):
        print("hello,wupeiqi")

obj=Foo()
