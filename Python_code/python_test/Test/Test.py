# -*-coding:utf-8 -*-

import sys
#mport os
from imp import reload
from collections import Iterable, Iterator

print "hello world"
print sys.path
reload(sys)
print sys.path[0].decode("gbk")

class test(object):
    def __init__(self):
        self.__num = 50

    @property
    def num(self):
        print "------getnum------"
        return self.__num

    @num.setter
    def num(self, new_num):
        print "------setnum------"
        self.__num = new_num

a = test()
#非迭代器不可使用next()取值
#print next(a)
a.num = 200
print a.num
#生成器是Iterator，Iterator占用空间小
print isinstance((x for x in range(10)), Iterator)

#列表不是迭代器，但是 是可迭代的
print isinstance([], Iterable)

a = [1,2,3]
print type(a)
b = iter(a)
print type(b)
print next(b)
#使用iter()函数可把list、dict、str等Iterable（可迭代的）变成Iterator（迭代器）
print isinstance(iter([1,2,3]), Iterator)

if isinstance([], Iterable):
    for a in "abc":
        print a


def test(num):
    print "----test----"
    def test_in(value):
        print num + value

        return
    return test_in

a = test(100)
a(10)


#动态添加方法 Begin
class Person(object):
    def __init__(self, name):
        self.name = name

def run(self):
    print("--%s正在跑--"%self.name)

from types import MethodType

p = Person("老王")

p.run = MethodType(run, p)

p.run()
#动态添加方法 End