# -*- coding:utf-8 -*-


import threading
import time
from socket import *

udpsocket = socket(AF_INET, SOCK_DGRAM)
udpsocket.bind(("", 8080))
feiQ = 2425
XP = 8101
ipdata = ("192.168.6.68", XP)
#udpsocket.sendto("", ipdata)

def socketSendMsg():
    #data = "1:12313213213:曾文君:Zzaniu:32:" + threading.current_thread().name + msg
    # decode(解码)的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
    # encode(编码)的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。
    while True:
        data = "1:12313213213:曾文君:Zzaniu:32:" + raw_input("\r>> ")
        senddata = data.decode("utf-8").encode("gbk")
        udpsocket.sendto(senddata, ipdata)

def socketRecvMsg():
    while True:
        recv = udpsocket.recvfrom(1024)
        data, listen = recv
        # data = udpsocket.recv(1024)
        print "\r<<", data.decode("gbk")
        print ">>",


#msg = raw_input("请输入你要发送的数据：")
#t = threading.Thread(target=socketSendMsg, args=(msg,), name="Thread-%d" % i)
t = threading.Thread(target=socketSendMsg)
t.start()
t2 = threading.Thread(target=socketRecvMsg)
t2.start()
t.join()
t2.join()
udpsocket.close()