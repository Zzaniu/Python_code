# -*-coding:utf-8 -*-

from multiprocessing import Process, Pool
import os
import time

def Test(name):
    for i in range(2):
        print("--Test--name = %s, pid = %d"%(name, os.getpid()))
        time.sleep(1)

#进程池
if __name__ == '__main__':
    po = Pool(10)
    for i in range(10):
        po.apply_async(Test, (i,))

    po.close()
    po.join()

# if __name__ == '__main__':
#     print("pid = %d"%(os.getpid()))
#     p = Process(target=Test, args=('xiaoming',))
#     p.start()
#     print p.pid
#     print p.name
#     print p.is_alive()
#     p.join()


#继承Process类
# class Process_Class(Process):
# #因为Process类本身也有__init__⽅法，这个⼦类相当于重写了这个⽅法，
# #但这样就会带来⼀个问题，我们并没有完全的初始化⼀个Process类，所以就不能使⽤从这个#最好的⽅法就是将继承类本身传递给Process.__init__⽅法，完成这些初始化操作
#     def __init__(self,interval):
#         Process.__init__(self)
#         self.interval = interval
#     #重写了Process类的run()⽅法
#     def run(self):
#         print("⼦进程(%s) 开始执⾏"%(os.getpid()))
#         t_start = time.time()
#         time.sleep(self.interval)
#         t_stop = time.time()
#         print("(%s)执⾏结束，耗时%0.2f秒"%(os.getpid(),t_stop-t_start))
#if __name__ == "__main__":
    # t_start = time.time()
    # print("当前程序进程(%s)"%os.getpid())
    # p1 = Process_Class(2)
    # #对⼀个不包含target属性的Process类执⾏start()⽅法，就会运⾏这个类s中的run()⽅法p1.start()
    # p1.start()
    # p1.join()
    # t_stop = time.time()
    # print("(%s)执⾏结束，耗时%0.2f"%(os.getpid(),t_stop-t_start))