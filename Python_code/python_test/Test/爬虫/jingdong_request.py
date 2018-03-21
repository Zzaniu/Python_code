#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-17 18:46:10
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$


from pytesser import pytesser
from selenium import webdriver
from lxml import etree
import requests
import pickle
import jsonpath
import json
import time
import os
import re
import sys


reload(sys)
sys.setdefaultencoding('utf-8')




def get_cookie_from_network():
    # url_login = 'https://plogin.m.jd.com/user/login.action'
    url_login = "https://home.m.jd.com/myJd/newhome.action"
    # url_login = "https://weibo.com"
    driver = webdriver.Chrome()
    # driver = webdriver.PhantomJS()
    time.sleep(2)
    driver.get(url_login)
    time.sleep(10)

    # driver.save_screenshot("weibo.png") #截屏

    driver.find_element_by_xpath('//*[@id="username"]').send_keys('451620411@qq.com') # 改成你的微博账号
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('!wenjunai93*') # 改成你的微博密码
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="loginBtn"]').click() # 点击登录
    time.sleep(5)
    # 获得 cookie信息
    cookie_list = driver.get_cookies()
    print cookie_list
    driver.quit()
    
    cookie_dict = {}
    for cookie in cookie_list:
        #写入文件
        f = open("./jingdongcookie/"+cookie['name']+'.jingdong', 'w')
        pickle.dump(cookie, f)
        f.close()

        if cookie.has_key('name') and cookie.has_key('value'):
            cookie_dict[cookie['name']] = cookie['value']

    return cookie_dict


def get_cookie_from_cache():
    cookie_dict = {}
    for parent, dirnames, filenames in os.walk("./jingdongcookie/"):
        print "parent = ", parent
        print "dirnames = ", dirnames
        print "filenames = ", filenames
        for filename in filenames:
            if filename.endswith('.jingdong'):
                with open("./jingdongcookie/" + filename, 'r') as f:
                    d = pickle.load(f)

                    if d.has_key('name') and d.has_key('value') and d.has_key('expiry'):
                        print "int(d['expiry']) = ", int(d['expiry'])
                        print "(int)(time.time()) = ", (int)(time.time())
                        expiry_date = int(d['expiry'])
                        if expiry_date > (int)(time.time()):
                            cookie_dict[d['name']] = d['value']
                        else:
                            print "cookie 过期..."
                            return {}

    return cookie_dict


def  get_cookie():
    cookie_dict = get_cookie_from_cache()
    if not cookie_dict:
        cookie_dict = get_cookie_from_network()
    
    return cookie_dict


def get_weibo_list(url):
    cookdic = get_cookie()

    # url = 'http://weibo.cn/stocknews88'
    headers = {'User-Agent': 'MQQBrowser/26Mozilla/5.0(Linux;U;Android2.3.7;zh-cn;MB200Build/GRJ22;CyanogenMod-7)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1'}
    timeout = 5
    # r = requests.get(url, headers=headers, cookies=cookdic, timeout=timeout).text
    # print r


if __name__ == "__main__":
    # get_weibo_list("https://home.m.jd.com/myJd/newhome.action")

    headers = {
        'User-Agent': 'MQQBrowser/26Mozilla/5.0(Linux;U;Android2.3.7;zh-cn;MB200Build/GRJ22;CyanogenMod-7)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1'}
    url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv49353&productId=5001175&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1"
    timeout = 5
    r = requests.get(url, headers=headers, timeout=timeout).text
    r = re.findall(r'"content":"(.*?)",', r)
    with open("XM_Note3.txt", "w") as f:
        for i in r:
            i += "\n"
            f.write(i)

