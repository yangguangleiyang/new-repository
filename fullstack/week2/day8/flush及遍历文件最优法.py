#_author:"yangqianfeng"
#date: 2020/6/27

# 忽闻鸟叫一声明，
# 缓起床前新天生。
# 欲问今日何所为，
# 一分辛苦一分才。

#flush() 方法是用来刷新缓存区的，即将缓存区的数据立刻写入文件，同时清空缓存区，不需要被动的等待输出缓存区写入。
#一般情况下，文件关闭后会自动刷新缓存区，但有时你需要在关闭前刷新它，这时就可以用flush()方法。
# import sys,time
# for i in range(30):
#     sys.stdout.write("*")
#     sys.stdout.flush()
#     time.sleep(0.2)

# f = open("小重山2","a",encoding="utf-8")
# f.truncate(6)  #truncate()是取文件前面六个字符，注意，打开方式一定要是append


# r+  w+  a+
#f = open("小重山2","r+",encoding="utf-8")
# print(f.readline())
# f.write("岳飞123")
#注意：
#r+：先读后写的话是在原有文本后添加, 因为读完后类指针已经在最末尾了，如果是先写后读的话，是从头开始覆盖式写

# f = open("小重山2","w+",encoding="utf-8")  #先清空列表
# f.write("岳飞")     #记住，写完之后光标定位在写完的位置，读的话只能往后读，所以需要seek一下
#
# print(f.tell())
# f.seek(0)
# print(f.readline())

# f = open("小重山2","a+",encoding="utf-8")
# f.write("是个英雄")       #在文件末尾追加
# print(f.readline())
#
# f.close()


#如果想替换中间部分的内容，只能重新写，因为字符串在磁盘位置是固定不变的。
# f_read = open("小重山","r",encoding="utf-8")
# f_write = open("小重山2","w",encoding="utf-8")
#
# number = 0
# for line in f_read:
#     number+=1
#     if number == 5:
#         line = "hello 岳飞\n"
#     if number == 6:
#         continue
#     f_write.write(line)
#
# f_read.close()
# f_write.close()


#with语句是防止忘记close ,当退出with代码行时自动关闭
with open("小重山","r",encoding="utf-8") as f_read,open("小重山2","w",encoding="utf-8") as f_write:
    number = 0
    for line in f_read:
        number += 1
        if number == 5:
            line = "hello world 岳飞\n"
        if number == 6:
            continue
        f_write.write(line)