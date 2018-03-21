#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-02 23:32:08
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$

import urllib
import urllib2
import re
from lxml import etree
import time
import sys
import threading
from multiprocessing import Pool
from threading import stack_size

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}

# 创建锁
mutex = threading.Lock()

def start_work(url, start_page, end_page):
    for i in range(start_page, end_page+1):
        fullurl = url + str(i)
        t = threading.Thread(target=dealurl, args=(fullurl,))
        t.start()
        if end_page == i:
            t.join()

    #     po.apply_async(dealurl, (fullurl,))
    #
    # po.close()
    # po.join()


def dealurl(url):
    request = urllib2.Request(url, headers=headers)
    print "url = ", url
    i = 0
    while i < 125:
        try:
            html = urllib2.urlopen(request).read()
            break
        except:
            if 124 == i:
                print "请求%s失败，程序退出" % url
                sys.exit(-1)
            print "第%d次请求%s失败，准备进行第%d次请求..." % (i+1, url, i+2)
            time.sleep(0.5)
            i += 1

    full_filename = "./Image/" + "91_" + "%s_html.html" % url[-2:]
    mutex.acquire()
    with open(full_filename, "wb") as f:
        f.write(html)
    mutex.release()
    content = etree.HTML(html)
    list_id = content.xpath('//table/tbody[contains(@id, "normalthread_")]/@id')
    link_lists_url = []
    print "len(list_id) = ", len(list_id)

    for i in list_id:
        link_lists_ding = content.xpath('//table/tbody[@id="%s"]//font'%i)

        if [] == link_lists_ding:
            continue

        int_beiding = re.search(r"\d+", link_lists_ding[0].text)
        if int(int_beiding.group()) > 100:
            print "int_beiding.group() = ", int_beiding.group()
            link_lists_url_temp = content.xpath('//table/tbody[@id="%s"]//span[contains(@id, "thread_")]/a/@href'%i)

            link_lists_url.append(link_lists_url_temp[0].split("&page")[0])

    link_lists_url = set(link_lists_url)
    print "len(link_lists_url) = ", len(link_lists_url)
    if len(link_lists_url) > 0:
        for sub_url in link_lists_url:
            url = "http://92.t9p.today/" + sub_url
            dealImageUrl(url)


def dealImageUrl(url):
    i = 0
    request = urllib2.Request(url, headers=headers)
    while i < 125:
        try:
            html = urllib2.urlopen(request).read()
            break
        except:
            if 124 == i:
                print "请求%s失败，程序退出" % url
                sys.exit(-1)
            print "第%d次请求%s失败，准备进行第%d次请求..." % (i+1, url, i+2)
            time.sleep(0.5)
            i += 1

    list_filename = re.findall(r'[^<a.*?]<img\ssrc=".*?"\sfile="(.*?)"', html)
    for src in list_filename:
        fullsrc = "http://92.t9p.today/" + src
        loadImage(fullsrc)


def loadImage(url):
    i = 0
    request = urllib2.Request(url, headers=headers)
    while i < 125:
        try:
            image = urllib2.urlopen(request).read()
            break
        except:
            if 124 == i:
                print "请求%s失败，程序退出" % url
                sys.exit(-1)
            print "第%d次请求%s失败，准备进行第%d次请求..." % (i + 1, url, i + 2)
            time.sleep(0.5)
            i += 1

    filename = url[-20:]
    full_filename = "./Image/" + filename
    mutex.acquire()
    with open(full_filename, "wb") as f:
        f.write(image)
    mutex.release()


if __name__ == "__main__":
    # 栈大小的设定将非常显著地影响python的内存占用，python多线程不设置这个值会导致程序占用大量内存，这对openvz的vps来说非常致命。
    # stack_size必须大于32768，实际上应该总要32768*2以上
    stack_size(32768 * 16)
    proxy_switch = False
    proxyhandler = urllib2.ProxyHandler({"http": "123.7.38.31:9999"})
    nullproxyhandler = urllib2.ProxyHandler({})
    if proxy_switch:
        opener = urllib2.build_opener(proxyhandler)
    else:
        opener = urllib2.build_opener(nullproxyhandler)
    urllib2.install_opener(opener)
    url = "http://92.t9p.today/forumdisplay.php?fid=19&page="
    start_page = int(raw_input("请输入起始页面: "))
    end_page = int(raw_input("请输入结束页面: "))
    start_work(url, start_page, end_page)
