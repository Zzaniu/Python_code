# -*- coding:utf-8 -*-


from socket import *

# TCP客户端 BEGIN
# ipaddr = ("192.168.6.68", 8080)
# tcpsocket = socket(AF_INET, SOCK_STREAM)
# tcpsocket.connect(ipaddr)
# tcpsocket.send("haha")
# tcpsocket.close()
# TCP客户端 END

#TCP服务器端 BEGIN
tcpsocket = socket(AF_INET, SOCK_STREAM)
#可重复使用绑定的信息
tcpsocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpsocket.bind(("", 12345))
tcpsocket.listen(3)

while True:
    tcpclient, addr = tcpsocket.accept()
    print "----------"
    print addr
    while True:
        data = tcpclient.recv(1024)
        if not data:
            break
        print data
        # tcpclient.send(data)
    tcpclient.close()
    break
tcpsocket.close()





#TCP服务器端 END
