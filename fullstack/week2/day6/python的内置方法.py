#_author:"yangqianfeng"
#date: 2020/6/24

st = "hello kitty {name} is {age}"

print(st.count("t"))  #统计元素次数
# print(st.capitalize()) #首字母大写

# print(st.center(20,"-")) #----hello kitty-----

#print(st.endswith("y"))  #判断是否以哪个字符串结尾，返回True 和 Flase
print(st.startswith("y"))  #判断是否以哪个字符串开始，返回True 和 Flase

#print(st.find("i"))  #查找到第一元素，并返回索引值
# print("eeeiuio".rfind("i"))   #从右边数

# print(st.format(name="alex",age=35))  #格式化输出  hello kitty alex
#print(st.format_map({"name":"alex","age":35}))

#print(st.index("t"))  he find yiyang

#print("323jdks".isalnum())  #判断是否是字母和数字

#print("333.33".isdigit())  #判断是否是数字  必须是整数，小数不行

#print(st.isidentifier())   #检查是否是非法变量

# print("erwe".islower())  #判断是否是全小写
# print("DIDI".isupper())  #判断是否是全大写

#print(" ".isspace())   #判断是否是空格

#print("My Title".istitle())  #判断是否是标题

# print("My Title".lower())     #将大写全部变为小写  小写不变
# print("My Title".upper())    #将小写全部变为大写，大写不变
# print("My Title".swapcase())    #将小写全部变为大写，大写变为小写
print("  kdkdk\n".strip())  #将空格和换行去掉
# print("eee")

# print("  kddkk   ".lstrip())  #只去掉左边的
# print("  kddkk   ".rstrip())  #只去掉右边的

#print("My Title  title".replace("tle","less",1))  #替换掉某些元素   1代表只替换第一个

# print("My Title  title".split("t"))  #将字符串通过t进行分割，分割成列表 ['My', 'Title', '', 'title']
# #将列表转换成字符串通过join方法
#
# print("My Title  title".rsplit("t",1))  #从右边开始分割，只分割一次

print("My Title  title".title())   #转换成标题的格式











