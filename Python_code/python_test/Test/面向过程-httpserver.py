# -*- coding:utf-8 -*-

from threading import Thread
from time import sleep
from multiprocessing import Process
from socket import *
# import os
#
# print os.getcwd()
# print os.listdir("./html")


def func(tcpclient):
    # print"tcpclient = ", id(tcpclient)
    data = tcpclient.recv(1024)
    #print data.decode("gbk")
    req_data = data.splitlines()
    req_start_line = req_data[0]
    req_data1 = req_start_line.split()
    print "---", req_data1
    print req_data
    try:
        f = open("./html/html1.html", "r")
        s_data = f.read()
        print "-----", s_data
        send_data = "HTTP/1.1 200 OK\r\n" + "Server: My Server\r\n" + "\r\n" + s_data
        tcpclient.send(send_data)
        print "--数据已发送--"
        tcpclient.close()
    finally:
        f.close()

def main():
    #TCP服务器端 BEGIN
    tcpsocket = socket(AF_INET, SOCK_STREAM)
    tcpsocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    tcpsocket.bind(("", 8000))
    tcpsocket.listen(3)
    while True:
        tcpclient, addr = tcpsocket.accept()
        # print"tcpclient = ", id(tcpclient)
        # print addr
        # 因为windows操作系统的原因，在Windows中，多进程multiprocessing使用的是序列化pickle来在多进程之间转移数据，
        # 而socket对象是不能被序列化的，但是在linux操作系统上却没问题，因为在linux上多进程multiprocessing使用的是fork，
        # 所以在windows上可以改用多线程。因为网络通信属于io密集型的操作，对cpu计算要求不高，不用多进程，用多线程就行。
        t = Thread(target=func, args=(tcpclient, ))
        t.start()

    tcpsocket.close()
    #TCP服务器端 END
if __name__ == "__main__":
    main()

