# encoding=utf-8
import requests
import json
import urllib

def getIPPortList():
    # host = "127.0.0.1"
    host = "180.76.247.130"
    types = 0
    count = 5
    catogary = "国内"
    url = 'http://%s:8000/?types=%s&count=%s&country=%s' % (host, types, count, urllib.quote(catogary))
    # print url
    r = requests.get(url)
    # print r.text
    ip_ports = json.loads(r.text)
    return ip_ports

ip_ports_list = getIPPortList()

for item in ip_ports_list:
    print item
    print ""