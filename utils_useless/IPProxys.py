#coding=utf-8

import requests
import json
import urllib
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from pprint import pprint
import random
import time
import os
import re

# type: 0: 高匿,1:匿名,2 透明
# count: 数量
# country: 国内， 国外
def getIPPortList(types, count, country):
    # host = "127.0.0.1"
    host = "180.76.247.130"
    url = 'http://%s:8000/?types=%s&count=%s&country=%s' % (host, types, count, urllib.quote(country))
    # print url
    r = requests.get(url)
    # print r.text
    ip_ports = json.loads(r.text)
    #print len(ip_ports)
    return ip_ports

pprint (getIPPortList(0, 100, "国内"))
exit()

def getAllHighScoreIP():
    proxydb = dtm.getCollection("spider", "proxyIpInfo")
    proxydb.drop()
    score_threshold = 9
    count = 100
    # count = 10000 
    for t in range(0,3):
        types = t
        for c in ["国内"]:
            country = c
            tmp_list = getIPPortList(types, count, country)
            for v in tmp_list:
                ip = v[0]
                port = v[1]
                score = v[2]
                if score < score_threshold:
                    continue
                ipport_dict = {
                    "type" : types,
                    "country" : country,
                    "ip" : ip,
                    "port" : port,
                    "score" : score,
                    "callcount" : 0
                }
                print (ipport_dict)
                dtm.dictToMongo(proxydb, ipport_dict)
                #break

#getAllHighScoreIP()

def getRandomIPPortList():
    ip_list = []
    proxydb = dtm.getCollection("spider", "proxyIpInfo")
    totalcount = proxydb.find().count()
    start = random.randint(0, totalcount)
    pickcount = min(100, totalcount-start)
    db_iter = proxydb.find().limit(pickcount).skip(start)
    for item in db_iter:
        ip = item["ip"]
        port = item["port"]
        country = item["country"]
        score = item["score"]
        # ip_port = str(ip) + ":" + str(port) + ":" + str(country) + ":" + str(score)
        ip_port = str(ip) + ":" + str(port)
        ip_list.append(ip_port)
        #print item
    return ip_list

#getRandomIPPortDict()

def updateIpCallCount(ip_dict):
    proxydb = dtm.getCollection("spider", "proxyIpInfo")
    for k, v in ip_dict.items():
        ip_port = k.split(":")
        ip = ip_port[0]
        port = ip_port[1]
        callcount = v
        proxydb.update({"ip":ip, "port":port}, {"$inc" : { "callcount" : callcount}})

def getProxyDriver(ip, port, driverType):
    driver = None
    ippPortStr = "%s:%s" % (ip, port)
    #print (driverType)
    if driverType == "chrome":
        chromeOptions = webdriver.ChromeOptions()
        args = '--proxy-server=http://%s' % ippPortStr
        chromeOptions.add_argument(args)  
        driver = webdriver.Chrome(chrome_options=chromeOptions)
    elif driverType == "firefox":
        profile = webdriver.FirefoxProfile() 
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", ip)
        profile.set_preference("network.proxy.http_port", port)
        profile.update_preferences() 
        driver = webdriver.Firefox(firefox_profile=profile)
    else:
        proxy_str = "--proxy=" + ippPortStr
        service_args = [proxy_str, '--proxy-type=http']
        driver = webdriver.PhantomJS(service_args=service_args)
    return driver

# driver = getProxyDriver("116.199.115.79", "80")
# driver = getProxyDriver("116.199.115.79", "80", driverType="phontomjs")
# driver.get('http://httpbin.org/ip')
# print driver.page_source
# driver.close()

def returnRandProxyIPDriver(driverType):
    ip_list = getRandomIPPortList()
    ipport = random.choice(ip_list)
    #print (ipport)
    ip = ipport.split(":")[0]
    port = ipport.split(":")[1]
    print ("return a proxy : %s" % ipport)
    return getProxyDriver(ip, port, driverType)

def getValidDriver(driverType):
    driver = None
    try:
        driver = returnRandProxyIPDriver(driverType)
        # driver = returnRandProxyIPDriver("firefox")
        driver.set_page_load_timeout(10) 
        driver.set_script_timeout(10)
        # print res
        driver.get("http://icanhazip.com")
    except Exception as e:
        print "exception occur when getting driver"
        return None
    html_str = driver.page_source
    #print html_str
    result, number = re.subn("<.*>", "", html_str)
    result = result.strip()
    if result == "":
        print "ip result is null"
        return None
    else:
        print "ip result is %s" % result
    return driver


if __name__ == '__main__':
    driver = getValidDriver("other")
    if driver == None:
        print "get driver error"
        exit()
    else:
        print "get driver ok"

    time.sleep(3)
    # time.sleep(10)
    driver.quit()