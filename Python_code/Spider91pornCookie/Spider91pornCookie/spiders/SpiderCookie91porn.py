# -*- coding: utf-8 -*-
import scrapy


class Spidercookie91pornSpider(scrapy.Spider):
    name = "SpiderCookie91porn"
    allowed_domains = ["91.91p23.space"]
    start_urls = (
        'http://91.91p23.space/login.php',
    )

    def parse(self, response):
        key = int(raw_input("请输入验证码: "))
        yield scrapy.FormRequest.from_response(
            response,
            formdata={
                "username": "hugong2",
                "password": "wenjunai93",
                "fingerprint": 4064814590,
                "fingerprint2": "1c1622f6f4c4021da40bcba6d8297077",
                "action_login": "Log In",
                "captcha_input": key,
                "x": 48,
                "y": 17,
                "language":"cn_CN"
            },
            callback = self.parse_page
        )

    def parse_page(self, response):
        print "=========1===" + response.url
        # with open("mao.html", "w") as filename:
        #    filename.write(response.body)
        url = "http://91.91p23.space/index.php"
        yield scrapy.Request(url, callback=self.parse_newpage)

    def parse_newpage(self, response):
        print "===========2====" + response.url
        with open("xiao.html", "w") as filename:
            filename.write(response.body)
