#python3
#encoding=utf-8  
import requests  
import re  
import time  
from bs4 import BeautifulSoup  
from pprint import pprint
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
headers = { 'User-Agent' : user_agent }  
#print soup.prettify()  

def sousuo(url):  
    r    = requests.get(url,headers=headers)  
    html = r.text  
  
    soup=BeautifulSoup(html, "lxml")  
    sou_dict = {}
    item_list = []
    count = []
    #print soup.prettify()  
    #获取热搜名称  
    i=1  
    for tag in soup.find_all(href=re.compile("Refer=top"),target="_blank"):  
        if tag.string is not None:  
            string = str(tag.string)
            # print (string)
            #print (title)
            item_list.append(title)
            i+=1  

    #获取热搜关注数  
    #return
    j=1  
    for tag in soup.find_all(class_="star_num"):  
        if tag.string is not None:  
            #print tag.string  
            #print(tag.string)
            count.append(tag.string)
            j+=1  

    for i in range(0, len(item_list)):
        sou_dict[item_list[i]] = count[i]

    return sou_dict
			
def getHotListFromWeb():
    sousuo('http://s.weibo.com/top/summary?cate=realtimehot')  

getHotListFromWeb()
