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


url = "https://s.hc360.com/?"

header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

word = {"w":"PVC机缝5号足球"}

word = urllib.urlencode(word)

full_url = url + word + "&mc=seller&ap=B&pab=B"

# full_url = "https://s.hc360.com/?w=PVC%BB%FA%B7%EC5%BA%C5%D7%E3%C7%F2&mc=seller&ee=7&ap=B&pab=B&t=1"
#
# request = urllib2.Request(full_url, headers=header)
#
# response = urllib2.urlopen(request)
#
# html = response.read().decode("gbk")
#
# print html

full_url = "https://s.hc360.com/?w=PVC%BB%FA%B7%EC5%BA%C5%D7%E3%C7%F2&mc=seller&ee=1&ap=B&pab=B&t=1&af=2&afadprenum=0&afadbeg=21"

request = urllib2.Request(full_url, headers=header)

response = urllib2.urlopen(request)

html = response.read().decode("gbk").encode('utf-8')
print html
list_url = re.search(r'公司名称.*?>(.*?\(.*\)).*?<', html)
print list_url.group(1)
shijian = re.search(r'注册时间.*?>(.*?)<', html)
print shijian.group(1)
ren = re.search(r'联系人.*?：(.*?)<', html)
print ren.group(1)
dizhi = re.search(r'经营地址.+?：(.*?)<', html)
print dizhi.group(1)
print "end"

# url = "https://b2b.hc360.com/supplyself/501243088.html"
#
# request = urllib2.Request(url, headers=header)
# response = urllib2.urlopen(request)
# html = response.read().decode("gbk")
# content = etree.HTML(html)
# list_id = content.xpath('//*[@id="productAttr"]/div[1]/div[1]/div[2]/p/a')
# url_list = content.xpath('//dd[@class="newName"]/a[contains(@title, "PVC")]/@href')
#
# print list_id[0].text
# print url_list[0]
# # print html