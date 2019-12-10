# coding=utf-8
#python2.7
import urllib2
import urllib
import util
from bs4 import BeautifulSoup
import re
from pprint import pprint
import time
import json
from pymongo import MongoClient

targeturl = "https://www.qiushibaike.com/"

url_dict = {
    "https://www.qiushibaike.com/" : "8hr",
    "https://www.qiushibaike.com/hot/" : "",
    "https://www.qiushibaike.com/text/" : "",
}

conn = MongoClient()
db = conn['spider']
qiubai_collections = db.qiubai

def genFilename():
    now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) 
    fullname = now + ".qiubai"
    return fullname

def genUrlList(targeturl, urltail, count):
    url_list = []
    if len(urltail) != 0:
        urltail += "/"
    for i in range(2, count+1):
        tmp = targeturl
        tmp += urltail + "page/" + str(i) + "/"
        #tmp += urltail + "page/" + "str(i)"
        url_list.append(tmp)
    return url_list

def getText(filename):
    htmlpage = open(filename, 'r').read()
    soup = BeautifulSoup(htmlpage, "html.parser")
    text = soup.get_text().encode("utf-8")
    return text

def getDiv(soup, class_name):
    div_list = soup.find_all('div', {'class': "class_name"})
    count = len(div_list)
    print count
    if count == 0:
        return []
    else:
        content = str(div_list[0])
        util.saveFile(class_name, content)
        text = getText(class_name)
        util.saveFile(class_name+".txt", text)
        return div_list[0]

def getPageCount(file):
    htmlpage = open(file, 'r').read()
    soup = BeautifulSoup(htmlpage, "html.parser")
    ul_list = soup.find_all('ul', {'class': "pagination"})
    li_list = ul_list[0].find_all('li')
    #print len(li_list)
    max = li_list[-2].get_text().strip(" ").strip("\n").strip()
    return int(max)
    #for v in li_list:
    #    print v.get_text()
    #li_list = ul_list[-1]
    #print li_list.get_text()

def getUrlContent(url):
    print "current processing url : %s" % url
    User_Agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
    req = urllib2.Request(url)
    req.add_header('User-Agent',User_Agent)
    try:
        response = urllib2.urlopen(req, timeout=5)
        data = response.read()
        filename = genFilename()
        util.saveFile(filename, data)
        print filename
        return filename
    except urllib2.URLError as e:
    	print "error"
        if hasattr(e, 'code'):
            print "Error code:", e.code
        elif hasttr(e, 'reasion'):
            print "Reason:", e.reason
        
        return "error"
    finally:
        if response:
            response.close()
    
#getUrlContent("qiubai")

def getDivContentById(url): 
    interval = util.genRandomTimeInterval()
    print "sleep randon time : %s" % interval
    time.sleep(interval)
    file = getUrlContent(url)
    htmlpage = open(file, 'r').read()
    soup = BeautifulSoup(htmlpage, "html.parser")
    div_list = soup.find_all('div', {'id': "content-left"})
    author_list = []
    for author in div_list[0].find_all("h2"):
        #print author.get_text().strip()
        author_list.append(author.get_text().strip())
    #print len(author_list)
    like_list = []
    for like in div_list[0].find_all("span", {"class":"stats-vote"}):
        likecount = like.find_all("i", {"class":"number"})[0].get_text()
        like_list.append(likecount)
    #print len(like_list)
    content_list = []
    for content in div_list[0].find_all("a", {"class":"contentHerf"}):
        content_list.append(content.get_text().strip())
    #print len(content_list)
    for i in range(len(author_list)):
        content_dict = {
            "author" : author_list[i],
            "like" : like_list[i],
            "content" : content_list[i]
        }
        json_obj = util.dictToJsonObj(content_dict)
        #print json_str
        qiubai_collections.insert(json_obj)

def getContent(key):
    #file = getUrlContent(key)
    #file = "qiubai.baike"
    #pageCount_int = getPageCount(file)
    for url, tail in url_dict.items():
        print url, tail
        # get first page
        file = getUrlContent(url)
        if file == "error":
            continue
        # get page count
        pageCount_int = getPageCount(file)
        util.removeFile(file)
        url_list = genUrlList(url, tail, pageCount_int)
        pprint (url_list)
        for u in url_list:
            getDivContentById(u)
            return

getContent("qiubai")