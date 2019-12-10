# coding=utf-8

"""  
Created on 2016-04-28 
@author: xuzhiyuan
功能: 爬取新浪微博的搜索结果,支持高级搜索中对搜索时间的限定
网址：http://s.weibo.com/
实现：采取selenium测试工具，模拟微博登录，结合PhantomJS/Firefox，分析DOM节点后，采用Xpath对节点信息进行获取，实现重要信息的抓取
"""

import time
import random
from pprint import pprint
from selenium import webdriver        

maxPageItemCount = 3

def returnDriver():
    #return webdriver.PhantomJS()
    return webdriver.Chrome()

def getContent(url, key, collection=""):

    #寻找到每一条微博的class
    driver = returnDriver()
    driver.get(url)
    nodes = driver.find_elements_by_xpath("//div[@class='WB_cardwrap S_bg2 clearfix']")
    print len(nodes)

    #在运行过程中微博数==0的情况，可能是微博反爬机制，需要输入验证码
    if len(nodes) == 0:
        print ("please input valid code!")
        #record the current processing key
        # util3.writeConfig("keyWords", key)
        #m.playRandomMusic()
        driver.quit() 

    head_dic = {}
    head_dic["key"] = key

    #global page
    #print (str(start_stamp.strftime("%Y-%m-%d-%H")))
    #print (u'页数:', page)
    #page = page + 1
    node_count = len(nodes)
    print (u'微博数量', node_count)

    for i in range(len(nodes)):
        if i == maxPageItemCount:
            break
        # time.sleep(random.randint(1,2))
        #dic[i] = []
        dic = head_dic
        
        #time.sleep(random.randint(3,10))
        time.sleep(random.randint(3,10))
        try:
            BZNC = nodes[i].find_element_by_xpath(".//div[@class='feed_content wbcon']/a[@class='W_texta W_fb']").text
        except:
            BZNC = ''
        print (u'博主昵称:', BZNC)
        dic["name"] = BZNC

        time.sleep(random.randint(3,10))
        try:
            BZZY = nodes[i].find_element_by_xpath(".//div[@class='feed_content wbcon']/a[@class='W_texta W_fb']").get_attribute("href")
        except:
            BZZY = ''
        print (u'博主主页:', BZZY)
        dic["mainpage"] = BZZY

        time.sleep(random.randint(3,10))
        try:
            WBNR = nodes[i].find_element_by_xpath(".//div[@class='feed_content wbcon']/p[@class='comment_txt']").text
        except:
            WBNR = ''
        dic["content"] = WBNR
        print ('微博内容:', dic["content"])
        #print (dic.keys())
        #dataToMongo.dictToMongo(collection, dic)
        print ('\n')
    driver.quit()

def getHotUrls():
    kv_dict = {}
    hoturl = "http://s.weibo.com/top/summary?cate=realtimehot"
    driver = returnDriver()
    driver.get(hoturl)

    entry = driver.find_element_by_xpath("//div[@id='pl_top_realtimehot']")
    hots = entry.find_elements_by_xpath(".//a")
    for hot in hots:
        href = hot.get_attribute("href")
        text = hot.text
        kv_dict[text] = href

    driver.quit()
    return kv_dict

if __name__ == "__main__":
    #collection = dataToMongo.getCollection("spider", "hotweibo")
    kv_dict = getHotUrls()
    pprint (kv_dict)
    counter = 0
    for k, v in kv_dict.items():
        counter += 1
        print counter
        print v
        time.sleep(1)
        getContent(v, k)
        
#GetSearchContent('35岁男子却因此丢了工作')
#GetSearchContent('青年兴则国兴')
