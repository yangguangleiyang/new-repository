
# def foo():
#     print("foo------")
#
# foo()

import time

def showtime(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print("spend time:%s"%(end-start))
    return inner

@showtime
def foo():
    print("fool------")
    time.sleep(2)
# foo = showtime(foo)   等价于@showtime  但是修饰器必须要放在被修饰代码的上面

foo()