import pymysql

#创建连接
conn=pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="123456",db="test1",charset="utf8")
#创建游标
cursor = conn.cursor()

#cursor.execute("insert into class(caption)values('一年级二班')")    #记住此处是单引号！！！

#参数传递，必须使用参数形式
#inp=input("请输入班级")
cursor.execute("insert into student(gender,class_id,sname)values(%s,%s,%s)",('男',2,'小丁'))
conn.commit()

#关闭游标
cursor.close()
#关闭连接
conn.close()



#备注
#增、删、改 需要有conn.commit()    查没有
#查询
cursor.execute("select * from student")
result=cursor.fetchall()   #打印出所有的
print(result)
result=cursor.fetchone()   #打印出第一个