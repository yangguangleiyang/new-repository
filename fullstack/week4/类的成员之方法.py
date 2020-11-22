class foo:

    def bar(self):  #普通方法
        print("bar")

    @staticmethod   #静态方法，可以不用传self
    def sta():
        print("123")

    @staticmethod    #静态方法也可以传参数
    def stac(a1,a2):
        print(a1,a2)

    @classmethod     #类方法，此方法用处不大，完全可以用静态方法实现
    def classmd(cls):
        #cls是类名
        print(cls)   #打印出来的是类名
        print("classmd")

foo.sta()        #通过类来调用方法，不用创建对象，因为创建对象占用内存
foo.stac(3,4)

foo.classmd()

#普通方法：保存在类中，通过对象来调用
#静态方法：保存在类中，通过类来调用
#类方法：保存在类中，通过类直接调用，cls指的是当前类