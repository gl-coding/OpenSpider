#-*-coding:utf8-*-

import re
import string
import sys
import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
from lxml import etree

reload(sys) 
sys.setdefaultencoding('utf-8')
# if(len(sys.argv) >=2):
#     user_id = (int)(sys.argv[1])
# else:
#     user_id = (int)(raw_input(u"请输入user_id: "))
user_id = 3280563191

cookie = {"Cookie": "_T_WM=b128a245d0a3c5951a6615c1f265e4b6; ALF=1510815724; SCF=ApMG0QZHAeN5NGOiElw4yTr9KasY0SQi4XZwzgcIlqJzHd9AKMrD4ORQ8QZUqW0GhgpRgYhrqACzsQJ0Ounr_Dw.; SUB=_2A2504cmgDeRhGedG71MR-SjOwjmIHXVULdforDV6PUJbktAKLU6gkW1YA_J1BE5d2jVe7-5Y9PN7U4xIqw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5iIr1xe8Epnr0fKBsXHX9k5JpX5K-hUgL.Fo2RSh271KqE1K-2dJLoI0qLxKBLB.2LB.2LxKML1KBL1-qLxKML1-2L1hBLxKBLB.zLBKeLxKMLBK5L1h2LxKML1h.L1hMt; SUHB=05i7VZ9mY5vEUQ; SSOLoginState=1508227568; H5_INDEX=0_all; H5_INDEX_TITLE=%E4%BA%BA%E7%94%9F%E7%9A%84%E4%BB%A3%E7%A0%81%E7%89%87; H5:PWA:UID=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1005053280563191%26featurecode%3D20000320%26fid%3D231051_-_fansrecomm_-_3280563191%26uicode%3D10000011"}
url = 'http://weibo.cn/u/%d?filter=1&page=1'%user_id

html = requests.get(url, cookies = cookie).content
print html
#html = requests.get(url).content
selector = etree.HTML(html)
pageNum = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])

result = "" 
urllist_set = set()
word_count = 1
image_count = 1

print u'爬虫准备就绪...'

for page in range(1,pageNum+1):
  if page == 4:
    break
  #获取lxml页面
  url = 'http://weibo.cn/u/%d?filter=1&page=%d'%(user_id,page) 
  lxml = requests.get(url, cookies = cookie).content

  #文字爬取
  selector = etree.HTML(lxml)
  content = selector.xpath('//span[@class="ctt"]')
  print content
  for each in content:
    text = each.xpath('string(.)')
    if word_count >= 4:
      text = "%d :"%(word_count-3) +text+"\n\n"
    else :
      text = text+"\n\n"
    result = result + text
    word_count += 1
    #exit()

  #图片爬取
  soup = BeautifulSoup(lxml, "lxml")
  urllist = soup.find_all('a',href=re.compile(r'^http://weibo.cn/mblog/oripic',re.I))
  first = 0
  for imgurl in urllist:
    urllist_set.add(requests.get(imgurl['href'], cookies = cookie).url)
    image_count +=1

fo = open("./%s"%user_id, "wb")
fo.write(result)
word_path=os.getcwd()+'/%d'%user_id
print u'文字微博爬取完毕'

link = ""
fo2 = open("./%s_imageurls"%user_id, "wb")
for eachlink in urllist_set:
  link = link + eachlink +"\n"
fo2.write(link)
print u'图片链接爬取完毕'

if not urllist_set:
  print u'该页面中不存在图片'
else:
  #下载图片,保存在当前目录的pythonimg文件夹下
  image_path=os.getcwd()+'\weibo_image'
  if os.path.exists(image_path) is False:
    os.mkdir(image_path)
  x=1
  for imgurl in urllist_set:
    temp= image_path + '\%s.jpg' % x
    print u'正在下载第%s张图片' % x
    try:
      urllib.urlretrieve(urllib2.urlopen(imgurl).geturl(),temp)
    except:
      print u"该图片下载失败:%s"%imgurl
    x+=1

print u'原创微博爬取完毕，共%d条，保存路径%s'%(word_count-4,word_path)
#print u'微博图片爬取完毕，共%d张，保存路径%s'%(image_count-1,image_path)
