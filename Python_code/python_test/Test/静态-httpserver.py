# -*- coding:utf-8 -*-

from threading import Thread
from time import sleep
from multiprocessing import Process
from socket import *
import re
import sys
# import os
#
# print os.getcwd()
# print os.listdir("./html")


class HTTPServer(object):
    '''HTTP类'''
    def __init__(self):
        self.rootpath = "./html"
        self.tcpsocket = socket(AF_INET, SOCK_STREAM)
        self.tcpsocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self, port):
        self.tcpsocket.bind(("", port))

    def start(self):
        self.tcpsocket.listen(3)
        while True:
            tcpclient, addr = self.tcpsocket.accept()
            # 因为windows操作系统的原因，在Windows中，多进程multiprocessing使用的是序列化pickle来在多进程之间转移数据，
            # 而socket对象是不能被序列化的，但是在linux操作系统上却没问题，因为在linux上多进程multiprocessing使用的是fork，
            # 所以在windows上可以改用多线程。因为网络通信属于io密集型的操作，对cpu计算要求不高，不用多进程，用多线程就行。
            t = Thread(target=self.func, args=(tcpclient,))
            t.start()

        self.tcpsocket.close()

    def func(self, tcpclient):
        # print"tcpclient = ", id(tcpclient)
        data = tcpclient.recv(1024)
        #print data.decode("gbk")
        req_data = data.splitlines()
        print "请求内容:", req_data
        requestheaderMethodLine = req_data[0]
        print "请求头:", requestheaderMethodLine
        req_filename = re.match(r"\w+ +(/[^ ]*) ", requestheaderMethodLine).group(1)
        print "请求文件名:", req_filename
        if "/" == req_filename:
            req_filename = "/html1.html"
        try:
            f = open(self.rootpath + req_filename, "r")
        except IOError:
            responseHeaderLines = "HTTP/1.1 404 not found\r\n"
            responsebody = "====sorry ,file not found===="
        else:
            responseHeaderLines = "HTTP/1.1 200 OK\r\n"
            responsebody = f.read()
            f.close()
        finally:
            response = responseHeaderLines + "\r\n" + responsebody
            tcpclient.send(response)
            print "--数据已发送--"
            tcpclient.close()


def main():
    httpserver = HTTPServer()
    httpserver.bind(8000)
    httpserver.start()

if __name__ == "__main__":
    main()

