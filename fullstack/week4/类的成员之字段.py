class Province:
    #静态字段，属于类
    country="中国"

    def __init__(self,name):
        #普通字段，属于对象
        self.name=name

hebei=Province("河北")
print(Province.country)  #通过类来访问静态字段
print(hebei.name)

