# !/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2, urllib
import ssl
import cookielib

ssl._create_default_https_context = ssl._create_unverified_context


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/61.0.3163.100 Safari/537.36"
}

c = cookielib.LWPCookieJar()
cookie = urllib2.HTTPCookieProcessor(c)
opener = urllib2.build_opener(cookie)

def login():
    req = urllib2.Request("https://kyfw.12306.cn/passport/captcha/captcha-image?login_site="
                          "E&module=login&rand=sjrand&0.4171279187210437")
    req.headers = headers
    codeImg = opener.open(req).read()
    fn = open("code.png", "wb")
    fn.write(codeImg)
    fn.close()
    reqest = urllib2.Request("https://kyfw.12306.cn/passport/captcha/captcha-check")
    reqest.headers = headers
    code = raw_input("请输入验证码：")
    data = {
        "answer": code,
        "login_site":"E",
        "rand":"sjrand"
    }
    data = urllib.urlencode(data)
    response = opener.open(reqest, data=data).read()
    print response
    req = urllib2.Request("https://kyfw.12306.cn/passport/web/login")
    req.headers = headers
    import user
    data = {
        "username": user.user,
        "password": user.pwd,
        "appid": "otn"
    }
    data = urllib.urlencode(data)
    html = opener.open(req, data).read()
    print html

login()