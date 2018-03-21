# -*- coding:utf-8 -*-

import time
from multiprocessing import Pool
from socket import *


def Socketfuc(msg, i):
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    port = 8090 + i
    udpSocket.bind(("", port))
    data = "1:12313213213:曾文君:Zzaniu:32:" + msg
    senddata = data.decode("utf-8").encode("gbk")
    ipdata = ("192.168.6.68", 2425)
    print "----------"
    udpSocket.sendto(senddata, ipdata)
    print senddata

if __name__ == "__main__":
    msg = raw_input("请输入你要发送的消息：")
    po = Pool(3)
    for i in range(5):
        po.apply_async(Socketfuc, (msg, i))

    po.close()
    po.join()