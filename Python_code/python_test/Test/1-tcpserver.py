# -*- coding:utf-8 -*-

from time import sleep
from multiprocessing import Process
from socket import *

# TCP客户端 BEGIN
# ipaddr = ("192.168.6.68", 8080)
# tcpsocket = socket(AF_INET, SOCK_STREAM)
# tcpsocket.connect(ipaddr)
# tcpsocket.send("haha")
# tcpsocket.close()
# TCP客户端 END

def func(tcpclient):
    print"tcpclient = ", id(tcpclient)
    while True:
        data = tcpclient.recv(1024)
        if not data:
            break
        print data.decode("gbk")
        tcpclient.send(data)
    tcpclient.close()

def main():
    #TCP服务器端 BEGIN
    tcpsocket = socket(AF_INET, SOCK_STREAM)
    tcpsocket.bind(("", 8000))
    tcpsocket.listen(3)
    sleep(5)
    while True:
        tcpclient, addr = tcpsocket.accept()
        print"tcpclient = ", id(tcpclient)
        print addr
        p = Process(target=func, args=(tcpclient,))
        p.start()
        p.join()
        tcpclient.close()

    tcpsocket.close()
    #TCP服务器端 END
if __name__ == "__main__":
    main()

