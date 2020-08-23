#_author:"yangqianfeng"
#date: 2020/8/16
# x=10
# def outer():
#
#     def inner():
#         print(x)
#     return inner
#
# f=outer()
# f()
#闭包就是内部函数+调用非全局变量且本地局域外的变量

#装饰器   修饰函数必须在被修饰函数之上
import  time
def logger(flag=""):
    def showtime(f):
        def inner(*args,**varge):
            statr=time.time()
            f(*args,**varge)
            end=time.time()
            print("spend time %s"% (end-statr))
            if flag=="true":
                print("日志打印")

        return inner
    return showtime

@logger("true")      #等价于先执行logger("true")函数，这个函数return showtime,相当于@showtime  等价于
#showtime=showtime(foo)
def foo(*args,**varge):
    print("一段代码")
    time.sleep(3)

foo(1,2,3,4,5,6)

