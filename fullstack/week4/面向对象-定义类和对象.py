#python 分为函数式和面向对象  但是java只能是面向对象
#函数
# def foo(name,age,gender):
#     print(name,age,gender)
#
# foo("yang",18,"nan")

#面向对象
# class bar:
#     def foo(self,arg):
#         print(self,self.name,self.age,self.gender,arg)
#
# z=bar()
#
# z.name="alex"
# z.age=18
# z.gender="nan"
# z.foo(555)
#
# z1=bar()
# z1.name="yang"
# z1.age=19
# z1.gender="nan"
# z1.foo(666)

#三大特性之封装

class person:

    def __init__(self,name,age):   #构造方法
        self.n=name
        self.a=age

    def show(self):
        print("%s--%s"%(self.n,self.a))

alex=person("alex",18)   #第一 创建了一个alex对象；  第二同时执行_init_函数
alex.show()

yang=person("yang",18)
yang.show()


