#-*- coding:utf-8 -*-

import urllib2
import re


def loadPage(url):
    '''
    :param url: 需要请求的url
    :return: 返回响应内容
    '''
    req = urllib2.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/61.0.3163.100 Safari/537.36")
    response = urllib2.urlopen(req)
    html = response.read()
    #先按照GBK解码，然后再UTF-8编码
    #new_html = html.decode('gbk', 'ignore').encode('utf-8')
    #'.*?':匹配一切    '(.*?)':取中间的一切
    pattern = re.compile(r'<h1.*?class="title">(.*?)</h1>', re.S)
    item_list = pattern.findall(html)

    return item_list

def writToFile(txt):
    '''
    写文件
    :param txt: 需要写入的文件
    :return: None
    '''
    #f = open("./myStory.txt", "a")
    #f.write(txt)
    #f.write("\n-----------------------------------------------------------------------------------------\n")
    #f.close()
    print txt


#url = raw_input("请输入贴吧网址:")
#url = "http://www.baidu.com"
url = "http://neihanshequ.com/"
print url
for item in loadPage(url):
    #print "="*300
    writToFile(item.replace(r"<p>", "").replace(r"</p>", "").strip())
