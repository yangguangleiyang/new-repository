#_author:"yangqianfeng"
#date: 2020/8/9

# def f(x,y):
#     print(x+y)
# f(3,5)

def add(*args):   # *args 为不定长参数 可接受很多参数
    print(args)
    sum=0
    for i in args:
        sum+=i
    print(sum)
add(1,2,4)