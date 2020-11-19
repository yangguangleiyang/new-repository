# class Foo:
#     def __init__(self):
#         self.name="a"
#
#     def bar(self):
#         print("bar")
#
#
#     @property     #这种方式就叫做属性，函数的方法，调取的方式却是调用的字段的方式
#     def per(self):
#         print("123")
#
# obj=Foo()
# obj.per       #重点看这行

#===============================================
#类的属性二
# class Foo:
#     def __init__(self):
#         self.name="a"
#
#     def bar(self):
#         print("bar")
#
#
#     @property     #这种方式就叫做属性，函数的方法，调取的方式却是调用的字段的方式
#     def per(self):
#         print("123")
#
#     @per.setter
#     def per(self,var):
#         print(var)
#
#     @per.deleter
#     def per(self):
#         print("666")
# obj=Foo()
# obj.per
# obj.per=456     #执行哪行就就去找对应的属性，此行对应@per.setter
# del obj.per     ##执行哪行就就去找对应的属性，此行对应@per.deleter

#==================================================================
#通过属性实现分页
class Pergination:
    def __init__(self,current_page):
        try:
            p=int(current_page)
        except Exception as e:   #这段不明白 后续了解吧
            p=1
        self.page=p
        #self.page=int(current_page)

    @property
    def start(self):
        va1=(self.page-1)*10
        return va1

    @property
    def end(self):
        va1=self.page*10
        return va1

li=[]
for i in range(1000):
    li.append(i)

while True:
    p=input("请输入要查看的页数")
    obj=Pergination(p)
    print(li[obj.start:obj.end])
