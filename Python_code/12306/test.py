# !/usr/bin/env python
# -*- coding:utf-8 -*-



import urllib
import urllib2
import time
from hashlib import md5, sha1, sha224, sha256, sha384, sha512

key = {"kw":"lol"}
print urllib.urlencode(key)

t = time.time()
print t
tt = (int(round(t * 1000)))
print tt
a = 3.456
print int(round(a*10))
ttt = 1520240009485
fun_list = [md5, sha1, sha224, sha256, sha384, sha512]
for fun in fun_list:
    encrypt = fun(str(ttt))
    # encrypt.update(str(ttt))
    up_ttt = encrypt.hexdigest()
    print up_ttt