
# 引入正则表达式：为了模糊匹配

#以下是精准匹配  通过find方法实现 返回的是索引值
# S="hello world"
# print(S.find("ll"))

#正则匹配
import re

# . 指通配符
# ret=re.findall("w..l","hello world")
# print(ret)

# ^ 只对开始进行匹配
# ret=re.findall("^h..o","hooojfdkafdja")
# print(ret)

# $ 只对最后进行匹配
# ret=re.findall("h..o$","hooojfdkafdjahiio")
# print(ret)

# * 重复匹配  *指0到无穷大
# ret=re.findall("ho*","hooujfdkafdjhoooooahiio")
# print(ret)   #['hoo', 'hooooo', 'h']

# + 重复匹配  指1到无穷次
# ret=re.findall("ho+","hooujfdkafdjhoooooahiio")
# print(ret)   #['hoo', 'hooooo']

# ？ [0,1]   指只有一个a或者没有a
# ret=re.findall("a?b","aaaabjddgfbjjab")
# print(ret)   #['ab', 'b', 'ab']

# {}  只有满足5个a才能输出
# ret=re.findall("a{5}b","aaaaaab")
# print(ret)
#
# ret=re.findall("a{1,5}b","aaaaaabababaab")
# print(ret)

#结论： * 等于{0，正无穷}   + 等于{1，正无穷}   ？等于{0,1}  推荐前者

# [] 字符集  或的关系
# ret=re.findall("a[c,d,e]x","acx")
# print(ret)

# ret=re.findall("[a-z]","acx")
# print(ret)

# [] 取消元字符的特殊功能  (\ ^  -  例外)
# ret=re.findall("[w,.]","fdsdwee.")
# print(ret)

# ^ 放在[]中 意思是取反
# ret=re.findall("[^t]","ddwetrre")
# ret=re.findall("[^t,e]","ddwetrre")  #取非t和非e

# \
# 反斜杠后边跟着元字符取消特殊功能
# 反斜杠后边跟着普通字符实现特殊功能

# \d  匹配任何十进制数，它相当于类 [0,9]
# \D  匹配任何非数字字符，他相当于类 [^0,9]
# \s  匹配任何空白字符，他相当于类[ \t\n\r\f\v]
# \S  匹配任何非空白字符，他相当于类[^ \t\n\r\f\v]
# \w  匹配任何字母数字字符，他相当于类[a-zA-Z0-9]
# \W  匹配任何非字母数字字符，他相当于类[^a-zA-Z0-9]
# \b  匹配一个特殊字符边界

# ret=re.findall("\d{11}","fdjsa323234324324323242") #匹配十一位手机号

#匹配出第一个满足条件的结果
# ret=re.search("s.b","fdjksafsabdddsvb").group()
# print(ret)

ret=re.search("a\.","a.efdf").group()
print(ret)






