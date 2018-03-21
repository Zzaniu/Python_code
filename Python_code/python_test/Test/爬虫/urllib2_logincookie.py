#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-01 16:56:13
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$


import urllib
import urllib2
import cookielib

url = "http://91.91p23.space/login.php"
url2 = "http://91.91p23.space/captcha.php"


# 通过CookieJar()类构建一个cookieJar()对象，用来保存cookie的值
cookie = cookielib.CookieJar()

# 通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie，参数就是构建的cookieJar()对象
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

# 构建一个自定义的opener
opener = urllib2.build_opener(cookie_handler)

# 通过自定义的opener的addheaders的参数，可以添加HTTP报头参数
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36")]

# 获取验证码图片
codeImg = opener.open(url2).read()
# print codeImg

fn = open("code.png", "wb")
fn.write(codeImg)
fn.close()

key = int(raw_input("请输入验证码: "))

# 需要登录的账户密码
data = {
    "username": "hugong2",
    "password": "wenjunai93",
    "captcha_input": key,
    "fingerprint": 563451053,
    "fingerprint2":"d53861a6015eaf888c921fc73f695e73",
    "action_login":"Log In",
    "x":51,
    "y":10
}

print data

data = urllib.urlencode(data)

print data

request = urllib2.Request(url, data=data)

response = opener.open(request)

print response.read()


