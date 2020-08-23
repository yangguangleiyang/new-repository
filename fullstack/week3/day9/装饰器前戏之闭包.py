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

def showtime(f):
    def inner():
        statr=time.time()
        f()
        end=time.time()
        print("spend time %s"% (end-statr))
    return inner

@showtime      #等价于foo=showtime(foo)
def foo():
    print("一段代码")
    time.sleep(3)

foo()

