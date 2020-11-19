class foo:

    def bar(self):  #普通方法
        print("bar")

    @staticmethod   #静态方法，可以不用传self
    def sta():
        print("123")

    @staticmethod    #静态方法也可以穿参数
    def stac(a1,a2):
        print(a1,a2)

    @classmethod     #类方法，此方法用处不大，完全可以用静态方法实现
    def classmd(cls):
        #cls是类名
        print(cls)   #打印出来的是类名
        print("classmd")

foo.sta()
foo.stac(3,4)

foo.classmd()