#getattr

class Foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        return "%s-%s" %(self.name,self.age)

obj=Foo("yang",18)
func=getattr(obj,"name")     #以字符串的形式获取对象中的成员
print(func)

func1=getattr(obj,"show")
print(func1)
r=func1()
print(r)

#hasattr
print(hasattr(obj,"name"))   #判断obj中是否有name,有则返回True,没有则返回False

#setattr
setattr(obj,"k1","v1")  #在obj中设置一个self.k1=v1
print(obj.k1)

#delattr
print(obj.name)
delattr(obj,"name")
print(obj.name)     #此时就报错了
