class F:

    def f1(self):
        print("F.f1")

    def f2(self):
        print("F.f2")

class S(F):

    def s1(self):
        print("S.s1")

#python中支持多继承
#1.左侧优先
#2.一条道走到黑
#3.同一个根时，根最后执行