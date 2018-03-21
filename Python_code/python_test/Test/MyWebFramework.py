#coding=utf-8

import time


HTML_ROOT_DIR = "./html"

class MyWebFramework(object):
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO", "/")
        if path.startswith("/static"):
            file_name = path[7:]
            try:
                f = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                status = "404 not found"
                headers = []
                responsebody = "====sorry ,file not found===="
            else:
                status = "200 OK"
                headers = [("Content-Type", "text/plain"), ("Server", "Zzaniu Server")]
                responsebody = f.read()
                f.close()

            start_response(status, headers)
            return responsebody

        for url, handler in self.urls:
            if path == url:
                return handler(env, start_response)

        status = "404 not found"
        headers = []
        responsebody = "====sorry ,file not found===="
        start_response(status, headers)
        return responsebody


def say_hello(env, start_response):
        status = "200 OK"
        headers = [("Content-Type", "text/plain"), ("Server", "Zzaniu Server")]
        start_response(status, headers)
        return "say hello"

def show_time(env, start_response):
        status = "200 OK"
        headers = [("Content-Type", "text/plain"), ("Server", "Zzaniu Server")]
        start_response(status, headers)
        return time.ctime()


urls = [
    ("/", show_time),
    ("/time", show_time),
    ("/sayhello", say_hello)
]

app = MyWebFramework(urls)