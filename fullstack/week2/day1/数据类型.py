
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