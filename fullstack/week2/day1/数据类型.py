
# 整数 int = integer
# 长整数   区别界限是2**30次方
# in py3中是不区分长整数和整数的
#
# 布尔只有两种状态：
#     真 True
#     假 False
#
# 字符串:

# age = 50
# flag = True #True和False必须大写
# while flag:
#     user_age = int(input("请输入您的年龄："))
#     if user_age == age:
#         print("yes")
#         flag = False
#     elif user_age > age:
#         print("it is bigger")
#     elif user_age < age:
#         print("it is smaller")
# print("end")

# --------------------------------------------------------------


# num = 1
# while num < 100:
#     if num%2 == 1:
#         print(num)
#     num += 1

# ---------------------------------------------------------------

# num=0
# while num<10:
#     num+=1
#     if num==3:
#         continue
#     print(num)

# ----------------------------------------------------------------------

#九九乘法表
# a = 1
# while a < 10:
#     b = 1
#     while b <= a:
#         print(b,"*",a,"=",a*b,end="\t")
#         #或者 print(string(b)+"*"+string(a)+"=",a*b,end="\n")
#         b+=1
#     print()
#     a += 1

# ---------------------------------------------------------------

# _user = "yangqianfeng"
# _password = "abc123"
#
# for i in range(3):
#     username = input("Username:")
#     password = input("Password:")
#
#     if username == _user and password == _password:
#         print("Welcome to %s login system"%_user)
#         break
#     else:
#         print("involid username or passworde")
#
# else:  #只有当for循环中次数正常执行结束，才会执行else部分，一旦出现中断，就不会执行了
#      print("登录次数过多")

# -----------------------------------------------------------------

# a = ["wuchao","jinxin","xiaohu","sanpang","liqiang"]
# print(a[3])
# print(a[1:3])
# print(a[0:])
# print(a[1::2])

# a.append("xiaohui")
# print(a)
# a.insert(2,"xiaoli")
# print(a)

#内置方法
# t=a.count("xiaohu")   #xiaohui出现的次数
# print(t)


# b=[1,2,3]
# c=[5,6,3]
# b.extend(c)   #把c的元素赋值一份给b
# print(b)
# print(c)

# ------------------------------------------
#元组和列表的区别：元组是不可变得，列表是可增删改除的
# a=(1,2,4,6,4,9)
# print(a[1:3])

# -----------------------------------------------
#字典
# dic={"name":"yang","age":"23","hobby":"girl"}
# dic["test"]=35
# print(dic)
#
# dic["name"]="yanglei"
# print(dic)


# dic={"name":"yang","age":"23","hobby":"girl"}
# print(dic["name"])
# print(dic.keys())
# print(dic.values())
# print(dic.items())

# dic={"name":"yang","age":"23","hobby":"girl"}
# del dic["name"]
# print(dic)

# dic.clear()
# print(dic)

#字典的循环遍历
# dic = {"name":"alex","age":35,"hobby":"girl"}
# for i in dic:
#     print(i)
    # print(i,dic[i])

# ----------------------------------------------
#集合
# li=[2,3,"alexe",2,34,5,3]
# s1=set(li)
# print(s1)

# -----------------------------------------
#浅拷贝
# a=[2,4,"alex",[5,6,89]]
# b=a.copy()
# print(a)
# print(b)

# a.append("xiaowu")
# print(a)
# print(b)

import copy
# a=[2,4,"alex",[5,6,89]]
# b=copy.copy(a)
# print(a)
# print(b)
#
# a.append("xiaohu")
# print(a)
# print(b)
#
# a[3][2]="dalin"
# print(a)
# print(b)

# b=copy.deepcopy(a)
# print(a)
# print(b)

# a.append("xiaohu")
# print(a)
# print(b)

# a[3][2]="xiaohu"
# print(a)
# print(b)

#-----------------------------------------------------------------
#函数
# def printinfo(arg1,*vartuple):
#     print("输出：")
#     print(arg1)
#     print(vartuple)
#     return
# printinfo(30,70,60,50)

#高阶函数  满足两个条件：1.函数名可以作为参数输入2.函数名可以作为返回值
# def f(n):
#     sum=1
#     for i in range(n):
#         sum=sum*(i+1)
#     # return sum
# print(f(5))


#裴波那契数列 递归写法
def peibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return peibo(n-1)+peibo(n-2)
print(peibo(8))

