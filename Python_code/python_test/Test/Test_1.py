# -*- coding:utf-8 -*-

import struct
from socket import *
import time
import os

requestFileData = struct.pack("!H5sb5sb", 1, "1.txt", 0, "octet", 0)
print requestFileData
li = [1,5,3,4]
lista = [55,66]
li.insert(10000, lista)
print li
