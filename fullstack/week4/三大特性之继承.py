class F:

    def f1(self):
        print("F.f1")

    def f2(self):
        print("F.f2")

class S(F):

    def s1(self):
        print("S.s1")

    def s2(self):
        print("F.f2")

    def f2(self):       #如果不想用父类的方法可以重写
        print("重写f2")
        super(S,self).f2()  #如果子类和父类都有同一方法，这样就可以同时调用了
        F.f2(self)         #同上面一样，写法不同
obj=S()
obj.s1()
obj.f2()