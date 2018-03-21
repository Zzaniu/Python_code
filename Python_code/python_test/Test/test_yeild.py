# coding=utf-8


from time import sleep
from greenlet import greenlet

def funA():
    i = 0
    while True:
        print i
        yield
        i += 1
        sleep(0.5)

def funB(a):
    num = 5
    while True:
        num -= 1
        print num
        a.next()
        if num == 0:
            return

def funC():
    i = 0
    while True:
        yield i
        i += 1
        # 去掉sleep（0.1）CPU资源占用会很大
        sleep(0.1)

def funD(a):
    num = 100000000
    while True:
        num -= 1
        print num
        print a.next()
        if num == 0:
            return

def funE():
    while 1:
        print "--A--"
        gr2.switch()
        sleep(0.5)


def funF():
    while 1:
        print "--B--"
        gr1.switch()
        sleep(0.5)

# a = funA()
# # a.next()
# # print a.next()
# funB(a)

# b = funC()
# funD(b)

gr1 = greenlet(funE)
gr2 = greenlet(funF)

gr1.switch()