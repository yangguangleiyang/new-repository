#_author:"yangqianfeng"
#date: 2020/6/18

#Alt + 问号 快捷键为批量注释

# 占位符
# %s = string
# %d = digit  整数
# %f = float  浮点数

name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")
if salary.isdigit():   #长的像数字
    salary = int(salary)   #将字符串转换为int类型
else:
    exit("must be input digit")  #退出程序

msg='''
-----info of %s----
Name:%s
Age:%s
Job:%s
Salary:%d  # %d要求必须输入数字
You will be retired in %s years
-------------end-------
'''%(name,name,age,job,salary,65-age)
print(msg)