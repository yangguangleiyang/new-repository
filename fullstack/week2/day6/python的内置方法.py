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

#print("My Title  title".title())   #转换成标题的格式



"""
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%2d"%(j,i,j*i),end="\t")
    print()

a = 1
while a <10:
    b = 1
    while b <= a:
        print("%d*%d=%2d"%(b,a,b*a),end="\t")
        b += 1
    a += 1
    print()
"""

#三级菜单登录

menu = {
    "北京":{
        "朝阳":{
            "望京":{
                "iqiyi":{},
                "快手":{},
                "优酷":{}
            },
            "三里屯":{},
            "大悦城":{}
        },
        "海淀":{},
        "通州":{}
    },
    "河北":{
        "衡水":{},
        "张家口":{},
        "邯郸":{}

    },
    "山东":{},
    "山西":{}
}

current_layer = menu
parent_layers = []
while True:
    for key in current_layer:
        print(key)
    choice = input("请输入选项：").strip()
    if len(choice) == 0:continue
    if choice in current_layer:
        parent_layers.append(current_layer)
        current_layer = current_layer[choice]

    elif choice == "b":
        if parent_layers:
            current_layer = parent_layers.pop()
    else:
        print("无此选项")





