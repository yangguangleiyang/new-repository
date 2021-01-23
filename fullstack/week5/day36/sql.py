# pymysql
#    --专门用于操作mysql的python模块
#    --Mysqldb(py3不支持)
'''
import pymysql

#创建连接
conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="123456",db="test1")
#创建游标
cursor = conn.cursor()

inp=input("请输入班级:")
cursor.execute('insert into class(caption)values(%s)',inp)
#cursor.execute('insert into class(caption,name,age)values(%s,%s,%s)',("自学全栈三班","鸭蛋","18"))

#r=cursor.execute('insert into class(caption)values("自学全栈一班")')  其中r为返回值，意思是受影响的行数
#print(r)


conn.commit()

#关闭游标
cursor.close()
#关闭连接
conn.close()

'''

#以上为增、删、改操作，都一样
#--------------------------------------
#以下为查询操作,(没有commit)

import pymysql

#创建连接
conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="123456",db="test1")
#创建游标
cursor = conn.cursor()

cursor.execute("select * from class")

# result=cursor.fetchall()   #取出所有的
# print(result)

result=cursor.fetchone()   #取出第一个
print(result)

# result=cursor.fetchmany(3)   #取出前三个
# print(result)


#关闭游标
cursor.close()
#关闭连接
conn.close()












