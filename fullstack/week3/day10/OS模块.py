
import os
#print(os.getcwd()) #获取当前工作目录  C:\Users\Administrator\PycharmProjects\new-repository\fullstack\week3\day10
#os.chdir("C:\Users")  #改变当前工作目录
#os.curdir  #返回当前目录
#os.pardir  #获取当前目录的父目录字符串名

#os.makedirs("abc\\yang\\test")  #生成目录  默认在当前工作目录下  一定要用\\

#os.removedirs("abc\\yang\\test")   #只删除空文件夹  递归删除
#os.mkdir("yang")  #创建单个文件
#os.mkdir("yang\\test")


# g=os.listdir(r"C:\Users\Administrator\PycharmProjects\new-repository\fullstack\week3\day10")
# print(g)  #打印出当前文件

#os.removedirs("abc\\yang\\test")   #只删除空文件夹  递归删除
#os.rmdir("yang\\test")  #删除单个文件夹
#os.remove("abc\\test.py")  #删除文件  不是文件夹

#os.rename("yang","yang1")   #重命名

# g=os.stat("abc")  #stat_result(st_mode=16895, st_ino=37436171902662567, st_dev=2860139438, st_nlink=1, st_uid=0, st_gid=0, st_size=0,
# # st_atime=1598870185, st_mtime=1598870049, st_ctime=1598837323)
# print(g.st_size)  #其中最重要的是大小

print(os.sep)  #取路径分隔符







