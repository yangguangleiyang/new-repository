# print("hello,world")
#
# t = input("请输入数字：")
# if int(t)>3:
#   print("大于等于3")
# else:
#   print("小于3")
#
# print("好好学习，天天向上")
# print("停车坐爱枫林晚")
# print("霜叶红于二月花")
# print("君不见黄河之水天上来")

# 九九乘法表
# a = 1
# while a < 10:
#     b = 1
#     while b <= a:
#         print(b,"*",a,"=",a*b,end="\t")
#         #或者 print(string(b)+"*"+string(a)+"=",a*b,end="\n")
#         b+=1
#     print()
#     a += 1

# 九九乘法表
for a in range(1, 10):
    for b in range(1, 10):
        if b <= a:
            print(b, "*", a, "=", b * a, end="\t")
            b = b + 1
    print()
