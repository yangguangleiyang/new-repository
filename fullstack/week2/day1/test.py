#print("hello world")
print("This is my first program in Pycharm")

'''age_of_princal = 56
guess_age = int(input("your age:"))
if guess_age == age_of_princal:
    print("yes")
else:
    print("it's wrong")
#----------------------------------
age = 50
flag = True #True和False必须大写
while flag:
    user_age = int(input("请输入您的年龄："))
    if user_age == age:
        print("yes")
        flag = False
    elif user_age > age:
        print("it is bigger")
    elif user_age < age:
        print("it is smaller")
print("end")
#也可以这样写： 使用break
age = 50

while True:
    user_age = int(input("请输入您的年龄："))
    if user_age == age:
        print("yes")
        break
    elif user_age > age:
        print("it is bigger")
    elif user_age < age:
        print("it is smaller")
print("end")


num = 1
while num < 100:
    if num%2 == 1:
        print(num)
    num += 1


#continue 跳过本次循环
num = 1
while num < 10:
    num += 1
    if num == 3:
        continue
    print(num)
'''
'''
while ... :
    .......
else:         #当while正常结束循环的时候才会执行
    ......

num = 1
while num <= 10:
    num += 1
    if num == 3:
        continue
    print(num)

num = 1
while num <= 10:
    if num == 3:
        continue
    print(num)
    num += 1
'''

'''不换行
print("hello world",end=" ")
print("hello world",end=" ")
print("hello world",end=" ")
print("\npython\npython\npython")
print("\tpython\tpython\tpython")
print()  #等价于print(end="\n")
'''
#总结： \n 的作用就是换行，其实end="\n"是默认不展示的，end=""双引号中表示以什么结束；\t表示缩进和tab一样
#制表符（也叫制表位)的功能是在不使用表格的情况下在垂直方向按列对齐文本。
'''
九九乘法表
a = 1
while a < 10:
    b = 1
    while b <= a:
        print(b,"*",a,"=",a*b,end="\t")
        #或者 print(string(b)+"*"+string(a)+"=",a*b,end="\n")
        b+=1
    print()
    a += 1
'''
'''
Height = int(input("Heitht:"))
Weight = int(input("Weight"))
num_Height = 1
while num_Height <= Height:
    num_weight = 1
    while num_weight <= Weight:
        print("#",end="\t")
        num_weight += 1
    print()
    num_Height += 1
'''
