#加密

import hashlib

# m=hashlib.md5()     #通过md5的算法加密
# m.update("hello world".encode("utf8"))
# print(m.hexdigest())    #作为十六进制数据字符串值   5eb63bbbe01eeed093cb22bb8f5acdc3
# print(m.digest())    # 作为二进制数据字符串值  b'^\xb6;\xbb\xe0\x1e\xee\xd0\x93\xcb"\xbb\x8fZ\xcd\xc3'

#另一种算法
s=hashlib.sha256()
s.update("hello world".encode("utf8"))
print(s.hexdigest())
