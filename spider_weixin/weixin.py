# coding=utf-8

"""  
Created on 2016-04-28 
@author: xuzhiyuan
功能: 爬取新浪微博的搜索结果,支持高级搜索中对搜索时间的限定
网址：http://s.weibo.com/
实现：采取selenium测试工具，模拟微博登录，结合PhantomJS/Firefox，分析DOM节点后，采用Xpath对节点信息进行获取，实现重要信息的抓取
"""

import time
import datetime
import re            
import os    
import sys  
import codecs  
import shutil
import urllib 
from selenium import webdriver        
from selenium.webdriver.common.keys import Keys        
import selenium.webdriver.support.ui as ui        
from selenium.webdriver.common.action_chains import ActionChains
import xlwt
import datetime
import random
from pprint import pprint
import util3
import IPProxys as proxy
import music as m
import util
import pdfkit

maxPageItemCount = 3

def returnDriver():
    # return webdriver.PhantomJS()
    return webdriver.Chrome()

def save_pdf(htmls, file_name):
    """
    把所有html文件转换成pdf文件
    """
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ]
    }
    pdfkit.from_file(htmls, file_name, options=options)

def genFilename(account, date):
    rank = random.randint(0, 1000)
    return account + date.replace("-", "_") + str(rank)

def savePage(url, rank):
    driver = returnDriver()
    driver.get(url)
    # js="var q=document.documentElement.scrollTop=10000"
    # driver.execute_script(js)
    time.sleep(30)
    text = driver.page_source
    filename = "weixin" + str(rank)
    file_html = filename + ".html"
    file_pdf = filename + ".pdf"
    util.saveFile(file_html, text)
    pdfkit.from_file(file_html, file_pdf)
    driver.quit()

def produceDate(datestr):
    #print datestr
    datestr = datestr.replace("年", "-").replace("月", "-")
    for it in datestr:
        if it != "-" and it.isdigit() == False:
            datestr = datestr.replace(it, "")
    #print datestr
    return datestr

def getLatestArtical(url):
    res = []
    pre = "http://mp.weixin.qq.com"
    driver = returnDriver()
    driver.get(url)
    eles = driver.find_elements_by_xpath("//div[@class='weui_msg_card']")
    # print len(eles)
    if 0 == len(eles):
        return []
    for e in eles:
        date = e.find_element_by_xpath(".//p[@class='weui_media_extra_info']").text
        date = produceDate(date)
        # break
        url = e.find_element_by_xpath(".//h4[@class='weui_media_title']").get_attribute("hrefs")
        fullurl = pre + url
        res.append((fullurl, date))
    time.sleep(2)
    driver.quit()
    return res

def getPublicAccount(account):
    res = []
    url = "http://weixin.sogou.com/"
    driver = returnDriver()
    driver.get(url)
    accountInput = driver.find_element_by_xpath("//input[@class='query']")
    accountInput.send_keys(account) #用户名
    searchPublic = driver.find_element_by_xpath("//input[@class='swz2']")
    searchPublic.click()
    time.sleep(3)
    publicAreas = driver.find_elements_by_xpath("//p[@class='tit']")
    if 0 == len(publicAreas):
        return {}
    for n in publicAreas:
        name = n.text
        # print name
        url = n.find_element_by_xpath(".//a").get_attribute('href')
        #driver.get(url)
        res.append((name, url))
        # break
    time.sleep(2)
    driver.quit()
    return res

def mainLogic():
    name = "csdn"
    items = getPublicAccount(name)
    print items
    return 
    for item in items:
        account = item[0]
        url = item[1]
        print account
        articles_list = getLatestArtical(url)
        #pprint(articles_list)
        counter = 0
        for article in articles_list:
            article_url = article[0]
            #savePage(article_url, counter)
            counter += 1
        break

if __name__ == "__main__":
    # collection = dataToMongo.getCollection("spider", "hotweibo")
    # kv_dict = getHotUrls()
    # #pprint (kv_dict)
    # counter = 0
    # for k, v in kv_dict.items():
    #     counter += 1
    #     print counter
    #     print v
    #     time.sleep(random.randint(10,30))
    #     getContent(v, collection, k)
    # getHotUrls()
    # getPublicAccount("hulktalk")
    # getPublicAccount("csdn")
    mainLogic()
