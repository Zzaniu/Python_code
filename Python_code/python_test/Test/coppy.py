# -*-coding:utf-8 -*-

from multiprocessing import Pool, Manager
import os
import time

def coppyFile(name, oldfilename, newfilwname, queue):
    try:
        #fr = open(oldfilename + '\\' + name, 'rb')
        #decode(解码)的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
        #encode(编码)的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。
        fw = open(newfilwname.encode("gbk") + "\\" + name, "ab")
        with open(oldfilename + '\\' + name, 'rb') as fr:
            for line in fr:
                fw.write(line)
        # msg = fr.read()
        # fw.write(msg)
    finally:
        # if fr:
        #     fr.close()
        if fw:
            fw.close()
            queue.put(name)


if __name__ == "__main__":
    oldfilename = raw_input("请输入你要拷贝的文件夹：")
    newfilwname = oldfilename + "-复件"
    newfilwname = newfilwname.decode("utf-8")
    os.mkdir(newfilwname)
    filename = os.listdir(oldfilename)
    queue = Manager().Queue()
    allnum = len(filename)
    start_time = time.time()
    pool = Pool(3)
    for name in filename:
        pool.apply_async(coppyFile, (name, oldfilename, newfilwname, queue))
    pool.close()
    num = 0
    while True:
        queue.get()
        num += 1
        print("coppy的进度是:%.2f%%"%(num * 100 / allnum))
        if num == allnum:
            break

    end_time = time.time()
    use_time = end_time - start_time
    print("需要拷贝文件个数为%s个，共拷贝文件%s个，使用时间为%.2f" % (allnum, num, use_time))