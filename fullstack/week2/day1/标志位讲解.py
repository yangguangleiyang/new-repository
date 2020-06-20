#_author:"yangqianfeng"
#date: 2020/6/20

exit_flag = False   #标志位
for i in range(10):
    if i < 5:
        continue
    print(i)
    for j in range(10):
        print("layer:",j)
        if j == 6:
            exit_flag = True
            break
    if exit_flag:
        break

