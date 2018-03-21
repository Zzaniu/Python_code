# !/usr/bin/env python
# -*- coding:utf-8 -*-
#使中文注释能够编译

import ssl
import urllib2
import json

ssl._create_default_https_context = ssl._create_unverified_context

def getTrainList():
    req = urllib2.Request("https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-11-10&"
                          "leftTicketDTO.from_station=SZQ&leftTicketDTO.to_station=IZQ&purpose_codes=ADULT")
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                "(KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    res = urllib2.urlopen(req)
    print type(res)
    html = res.read()
    result = json.loads(html)
    return result["data"]["result"]

#[23] = 软卧
#[26] = 无座
#[28] = 硬卧
#[29] = 硬座
#[30] = 二等座
#[31] = 一等座


def getWuZuo(alist):
    try:
        if int(alist[26]) > 0:
            print "  无座余票%d张" % int(alist[26])
        else:
            print "  无座无票"
    except:
        if alist[26] == u"有":
            print "  无座有票"
        else:
            print "  无座无票"

def getYingZuo(alist):
    try:
        if int(alist[29]) > 0:
            print "  硬座余票%d张" % int(alist[29])
        else:
            print "  硬座无票"
    except:
        if alist[29] == u"有":
            print "  硬座有票"
        else:
            print "  硬座无票"

def getYingWo(alist):
    try:
        if int(alist[28]) > 0:
            print "  硬卧余票%d张" % int(alist[28])
        else:
            print "  硬卧无票"
    except:
        if alist[28] == u"有":
            print "  硬卧有票"
        else:
            print "  硬卧无票"

def getRuanWo(alist):
    try:
        if int(alist[23]) > 0:
            print "  软卧余票%d张" % int(alist[23])
        else:
            print "  软卧无票"
    except:
        if alist[23] == u"有":
            print "  软卧有票"
        else:
            print "  软卧无票"

def getErDengZuo(alist):
    try:
        if int(alist[30]) > 0:
            print "  二等座余票%d张" % int(alist[30])
        else:
            print "  二等座无票"
    except:
        if alist[30] == u"有":
            print "  二等座有票"
        else:
            print "  二等座无票"

def getYiDengZuo(alist):
    try:
        if int(alist[31]) > 0:
            print "  一等座余票%d张" % int(alist[31])
        else:
            print "  一等座无票"
    except:
        if alist[31] == u"有":
            print "  一等座有票"
        else:
            print "  一等座无票"

dict_1 = {'name':'xiaoming', 'name2':"xiaowang"}
encoded_json = json.dumps(dict_1)
dict_2 = json.loads(encoded_json)
print type(dict_1), dict_1
print type(encoded_json), encoded_json
print type(dict_2), dict_2

a = 0
for i in getTrainList():
    tmp_list = i.split("|")
    #for temp in tmp_list:
    #    a += 1
    #    print "a = %r, temp = %s"%(a, temp)
    #a = 0
    print "列车 = ", tmp_list[3]
    getWuZuo(tmp_list)
    getYingZuo(tmp_list)
    getYingWo(tmp_list)
    getRuanWo(tmp_list)
    getErDengZuo(tmp_list)
    getYiDengZuo(tmp_list)
