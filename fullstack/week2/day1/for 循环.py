#_author:"yangqianfeng"
#date: 2020/6/19

# for i in range(3):
#     print(i)
#运行结果为 0 1 2

# for i in range(1,3):    i 代表次数
#     print(i)
# 运行结果为：1 2  （取左不取右）

# for i in range(1,10,2):   #其中 2 为步长
#     print(i)
# 运行结果为：1 3 5 7 9  （取左不取右）

#break语句的使用：
#
# _user = "yangqianfeng"
# _password = "abc123"
#
# password_authentication = False  # 这叫做标志位
#
# for i in range(3):
#     username = input("Username:")
#     password = input("Password:")
#
#     if username == _user and password == _password:
#         print("Welcome to %s login system"%_user)
#         password_authentication = True
#         break
#     else:
#         print("involid username or passworde")
#
# if not password_authentication:
#     print("登录次数过多")

#以上案例也可以用 for  else 来完成
#
_user = "yangqianfeng"
_password = "abc123"

for i in range(3):
    username = input("Username:")
    password = input("Password:")

    if username == _user and password == _password:
        print("Welcome to %s login system"%_user)
        break
    else:
        print("involid username or passworde")

else:  #只有当for循环中次数正常执行结束，才会执行else部分，一旦出现中断，就不会执行了
     print("登录次数过多")
"""
#用while循环完成

_user = "yangqianfeng"
_password = "abc123"

counter = 0
while counter < 3:
    username = input("Username:")
    password = input("Password:")

    if username == _user and password == _password:
        print("Welcome to %s login system"%_user)
        break
    else:
        print("involid username or passworde")
    counter += 1

else:  #只有当for循环中次数正常执行结束，才会执行else部分，一旦出现中断，就不会执行了
    print("登录次数过多")
"""

