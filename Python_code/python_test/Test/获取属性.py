# coding=utf-8


class Foo(object):
    def __init__(self):
        pass

    def __str__(self):
        return "Hello World"

    # 查找属性的时候自己的__dict__中和父类的__dict__中找不到的时候，就会执行__getattr__
    def __getattr__(self, item):
        print item
        return self


a = Foo()
print a.thinks.different.zzaniu
