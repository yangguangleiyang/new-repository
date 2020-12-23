import socket
sk=socket.socket()
print(sk)

address=("127.0.0.1",8888)
sk.bind(address)
sk.listen(3)   #最多排队排三个，多出的不允许被连接
print("waiting...")
while True:
    conn,addr=sk.accept()
    print(addr)   #此处接收的是客户端的ip和端口

    while True:
        data=conn.recv(1024)
        print(str(data,"utf8"))
        if not data:
            break
        inp=input(">>>")
        conn.send(bytes(inp,"utf8"))
sk.close()
