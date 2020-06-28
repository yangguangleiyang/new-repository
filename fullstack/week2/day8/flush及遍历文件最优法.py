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

f = open("小重山2","a",encoding="utf-8")
# f.truncate(6)  #truncate()是取文件前面六个字符，注意，打开方式一定要是append
#
# f.close()

