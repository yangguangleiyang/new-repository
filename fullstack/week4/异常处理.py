# try:
#     #代码块
#     pass
# except Exception as e:
      #e是Exception对象，对象中封装了上面代码块中的错误信息
#     #上述代码块如果出错，自动执行当前块的内容

# while True:
#     try:
#         inp=input("请输入序号:")
#         i=int(inp)
#     except Exception as e:
#         #print(e)  #可以输出上述模块的错误信息
#         i=1
#     print(i)

#================================================
# try:
#     li=[11,22,33]
#     li[999]
# except IndexError as e:    #如果报这种错误，会执行这块的代码
#     print("IndexError")
# except ValueError as e:
#     print("ValueError")
# except Exception as e:
#     print("Exception")
#
# else:          #如果最上面代码执行没问题，则执行这块代码
#     print("123")
# finally:       #不管最上面代码执行成功或者不成功，都会执行这块代码
#     print("456")

#================================
#主动触发异常
def db():
    return False
def index():
    try:
        r=input(">>")
        int(r)

        result=db()
        if not result:
            #r=open("log","a")
            #r.writte("数据库处理错误")
            raise Exception("数据库处理错误")   #主动触发异常，目的是把错误信息写到下面的日志，省略了上面两行diam
    except Exception as e:
        str_error=str(e)
        print(str_error)
        r=open("log","a")   #打开文件写日志
        r.write(str_error)

index()