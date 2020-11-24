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
class Foo:
    def __init__(self):
        pass
    def __int__(self):
        return 111
    def __str__(self):
        return "alex"

obj=Foo()
print(obj,type(obj))

#int 对象，自动执行对象的__int__方法，并将返回值赋值给int对象
r=int(obj)
print(r)

i=str(obj)
print(i)


# class Foo:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#     def __str__(self):
#         return self.name
# obj=Foo('alex',18)
# print(obj)  #print默认调用了str方法，print(str(obj))
