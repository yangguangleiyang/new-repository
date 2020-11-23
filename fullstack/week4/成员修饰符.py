#公有字段、方法
#私有字段、方法
#
class F:
    def __init__(self):
        self.name=123
        self.__gene=555
class S(F):
    def __init__(self,name):
        self.name=name
        self.__age=18
        super(S, self).__init__()

    def show(self):
        print(self.name)
        print(self.__age)
        # print(self.__gene)

obj=S("yang")
obj.show()

#总结：
#1.私有字段或方法不能被外部调用（外部指的是类），类内可以调用，但是可以间接调用，被同类里面别的方法调用后，再创建对象，
#调用别的方法

class A:
    def test(self):
        print("yang")

class B(A):
    def test(self):
        print("xiaoyang")
        super(B,self).test()   #子类和父类同时调用
obj=B()
obj.test()