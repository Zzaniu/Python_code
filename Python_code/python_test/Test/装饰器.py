# -*-coding:utf-8 -*-


#装饰器原理 begin
def w1(func):
    def inner():
        print("---正在验证权限----")
        func()
    return inner

def f1():
    print("---f1---")

#innerFunc = w1(f1)
#innerFunc()

f1 = w1(f1)
f1()
#装饰器原理 end


#定义函数：完成包裹数据
def makeBold(fn):
    print "装饰器1"
    def wrapped():
        print("----1---")
        return "<b>" + fn() + "</b>"
    return wrapped

#定义函数：完成包裹数据
def makeItalic(fn):
    print "装饰器2"
    def wrapped():
        print("----2---")
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold
@makeItalic
def test3():
    print("----3---")
    return "hello world-3"

ret = test3()
print(ret)


def func(functionName):
    print("---func---1---")     #只要Python解释器执行到@func，那么这行代码就会被执行
    def func_in(*args, **kwargs):#采用不定长参数的方式满足所有函数需要参数以及不需要参数的情况
        print("---func_in---1---")
        ret = functionName(*args, **kwargs)#这个地方,需要写*以及**,如果不写的话,那么args是元祖,而kwargs是字典
        print("---func_in---2---")
        return ret

    print("---func---2---")
    return func_in

@func
def test(a, b, c):
    print("----test-a=%d,b=%d,c=%d---"%(a,b,c))

@func
def test2(a, b, c, d):
    print("----test-a=%d,b=%d,c=%d,d=%d---"%(a,b,c,d))

@func
def test3():
    print("----test3----")

test(11,22,33)

test2(44,55,66,77)

test3()




#生成器 Begin
#生成器：仅仅是保存了一套生成特殊数值的代码，并不会执行，只有当去调它的时候才开始执行计算一个新的值并返回
def creatNum():
    print("---start---")
    a,b = 0,1
    for i in range(5):
        print("---1---")
        yield b
        print("---2---")
        a, b = b, a+b
        print("---3---")
    print("---stop---")

a = creatNum()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
#生成器 End