# -*- coding: UTF-8 -*-
import urllib2
from http import cookiejar

if __name__ == '__main__':

    #设置保存cookie的文件，同级目录下的cookie.txt
    filename = 'cookie.txt'
    #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookiejar.MozillaCookieJar(filename)
    #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler = urllib2.HTTPCookieProcessor(cookie)
    #通过CookieHandler创建opener
    opener = urllib2.build_opener(handler)
    #此处的open方法打开网页
    response = opener.open('http://m.weibo.com')
    #保存cookie到文件
    cookie.save(ignore_discard=True, ignore_expires=True)
