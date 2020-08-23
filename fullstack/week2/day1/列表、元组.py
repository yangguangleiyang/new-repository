#_author:"yangqianfeng"
#date: 2020/6/20

#列表
a = ["wuchao","jinxin","xiaohu","sanpang","liqiang"]
#print(a)

#查   切片
# print(a[3])
#print(a[1:3])  #切记 顾头不顾尾 实际输出只有1、2
# print(a[1:])  #取到最后
# print(a[1:-1]) #取到最后的倒数第二值
# print(a[1::2]) #其中2为步长
# print(a[3::-2]) #b表示从右边到左边倒着输出
# print(a[-1::-1])  #-1代表倒数第一个。-2代表倒数第二个

#增  append insert
#append 自动在列表结尾自动添加
# a.append("xiaowang")
# print(a)
#insert 可以插入到任意位置
# a.insert(2,"xueppeng")
# print(a)

#改
# a[2] = "zhangsan"
# a[1:3] = ["yangchao","lihua"]
# print(a)

#删除  remove pop  del
# a.remove("liqiang")
# print(a)

# b=a.pop(1) #通过索引来删除，还可以返回索引对应的元素值
# print(a)
# print(b)
# a.pop()  #代表默认删除列表中最后一个元素
#del a[0]
#print(a)

#内置方法
#count 查元素出现的次数
#a = ["wuchao","jinxin","xiaohu","sanpang","liqiang","xiaohu","sanpang","liqiang"]
# t = a.count("liqiang")
# print(t)

#extend
# a=[1,2,3]
# b=[4,5,6]
# a.extend(b) #把b的元素复制一份到a
# print(a)
# print(b)

#index  通过元素找到索引
# a = ["wuchao","jinxin","xiaohu","sanpang","liqiang"]
# t=a.index("sanpang")
# print(t)

# reverse  将列表内元素倒着排序
# a = ["wuchao","jinxin","xiaohu","sanpang","liqiang"]
# a.reverse()
# print(a)

#sort  对列表内容进行排序
# a = [5,8,3,7,5,4,3]
#a = ["wuchao","jinxin","xiaohu","sanpang","liqiang"]
# a.sort()
# print(a)


