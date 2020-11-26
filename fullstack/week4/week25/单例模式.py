# class Foo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print(self.name,self.age)
#
# obj=Foo()  #obj是类的对象，也叫做实例
# obj1=Foo()   #又创建了一个实例

#单例的意思是使用同一个实例（对象）进行调用


"""
class Foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)

v=None
while True:
    if v:
        v.show()
    else:
        v=Foo("yang",18)
        v.show()
"""


a=1
for i in range(10):

    if a<=i:
        print(a,"*",i,"=",a*i,end="")
    a=a+1
