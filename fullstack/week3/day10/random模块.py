#随机数
import random
# print(random.random())  #随机生成  不会超过1
# print(random.randint(1,6)) #包括1和6
# print(random.choice("hello"))
# print(random.randrange(1,6)) #不包括6

#随机生成验证码
def v_code():
    code=""
    for i in range(5):
        add_num=random.choice([random.randrange(10),chr(random.randrange(65,122))])
        code+=str(add_num)
    print(code)
v_code()
