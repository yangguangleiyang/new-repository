#_author:"yangqianfeng"
#date: 2020/6/18

#ctrl + /    快捷键为批量注释

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
----welcome %s---
name1:%s
age1:%s
job1:%s
salary1:%s
You will be retired in %s years
'''%(name,name,age,job,salary,65-age)
print(msg)