#_author:"yangqianfeng"
#date: 2020/6/21

#元组是只可读的，查询的方式和列表是一样的
# a=(1,2,4,6,4,9)
# print(a[1:3])

#购物车程序
product_list = [
    ("computer",5000),
    ("bycle",2000),
    ("telse",900000),
    ("Phtonbook",80),
    ("banner",20)
]
shopping_car = []
saving = input("plese input your money:")
if saving.isdigit():
    saving = int(saving)

    while True:
        for i,v in enumerate(product_list,1): #enumerate将索引打印出来，1代表从索引起始位置
            print(i,"<<<<<",v)

        choice = input("请输入您的选项(退出按q)：")
        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= len(product_list):
                pitem = product_list[choice-1]
                if saving > pitem[1]:
                    saving -= pitem[1]
                    shopping_car.append(pitem)
                else:
                    print("您的余额不足,还剩%s元"%saving)
                print(pitem)
            else:
                print("编码不存在")
        elif choice == "q":
            print("-----您已购买如下商品----")
            for i in shopping_car:
                print(i)
            print("您还剩%s元"%saving)

            break

        else:
            print("请输入正确数据编号")
else:
    print("请输入数字")