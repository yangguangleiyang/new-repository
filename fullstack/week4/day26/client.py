import socket
sk=socket.socket()
print(sk)

address=("127.0.0.1",8000)    #127.0.0.1为回环地址，代指本机ip
sk.connect(address)

while True:
    inp=input(">>>")
    if inp=="exit":
        break
    sk.send(bytes(inp,"utf8"))
    data=sk.recv(1024)
    print(str(data,"utf8"))
sk.close()