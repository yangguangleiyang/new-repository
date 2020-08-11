#_author:"yangqianfeng"
#date: 2020/6/26

#读文件
# f = open("小重山","r",encoding="utf-8")
# date=f.read(5)   #5代表前五个字符
# print(date)

#写文件
#f = open("小重山","w",encoding="utf-8")   #这段叫做文件句柄
# f.write("hello world")  #先将之前的清空掉，然后再赋值新的
# f.write("alex")   #hello worldalex

#f = open("小重山2","w",encoding="utf-8")#如果没有小重山2，则会自动创建一个文件

#追加内容
# f = open("小重山","a",encoding="utf-8")
# f.write("hello world")

#关闭文件  最后一定要关闭文件
# f.close()

#注意 ： 不能在同一时刻，被两个人拿到

#文件操作具体方法
f = open("小重山","r",encoding="utf-8")
#print(f.readline())  #打出第一行
b = f.readlines()
print(b)  #打印全部内容
#运行结果是列表：['昨夜寒蛩不住鸣。\n', '惊回千里梦，已三更。\n', '起来独自绕阶行，\n',
# '人悄悄，帘外月胧明。\n', '白首为功名，旧山松竹老，阻归程。\n', '欲将心事付瑶琴，\n', '知音少，弦断有谁听。']

#给某一行加内容
# number = 0
# for i in f.readlines():
#     number += 1
#     if number == 6:
#         i = "".join([i.strip(),"11111"])
#     print(i.strip())
#
# f.close()


# f = open("小重山","r",encoding="utf-8")
# # for i in f:   #目的是用哪个就取出哪个，这是for内部将f做成一个迭代器
# #     print(i.strip())
#
# print(f.tell())
# print(f.read(5))
# print(f.tell())  #英文代表一个字符，中文代表三个字符，所以输出是15
#
# print(f.seek(0))  #seek的作用是将光标跳到指定位置
# print(f.read(6))
#
# f.close()