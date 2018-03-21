#coding=utf-8

import time

def application(env, start_response):
    # 打印当前时间
    status = "200 OK"
    headers = [("Content-Type", "text/plain"), ("Server", "Zzaniu Server")]
    start_response(status, headers)

    return time.ctime() + "\r\nZzaniu\r\n"
