#time 模块
import time

# print(time.time())  #1598583201.2656531 从unix诞生到现在的秒  叫做时间戳
# time.sleep(3)

print(time.gmtime())  #time.struct_time(tm_year=2020, tm_mon=8, tm_mday=28, tm_hour=5,
# tm_min=57, tm_sec=8, tm_wday=4, tm_yday=241, tm_isdst=0)  结构化时间 英国的时间
print(time.localtime()) #time.struct_time(tm_year=2020, tm_mon=8, tm_mday=28, tm_hour=13,
# tm_min=57, tm_sec=56, tm_wday=4, tm_yday=241, tm_isdst=0)  本地时间

#设置时间格式
# g=time.localtime()
# print(time.strftime("%Y--%m--%d %H:%M:%S",g))  #2020--08--28 14:00:07

#也可以用这种方式  这种用的最多
import datetime
print(datetime.datetime.now())