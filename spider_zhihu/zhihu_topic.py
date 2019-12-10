# coding=utf-8

import time
from selenium import webdriver        
from selenium.webdriver.common.keys import Keys        
import selenium.webdriver.support.ui as ui        
from selenium.webdriver.common.action_chains import ActionChains
from pprint import pprint

#先调用无界面浏览器PhantomJS或Firefox    
#driver = webdriver.PhantomJS()
driver = webdriver.Chrome()

def getRelatedSinglePage(url):
    driver.get(url)
    #歇两秒
    time.sleep(2)

    #找到入口xpath节点
    entrys = driver.find_elements_by_xpath("//div[@class='Card-section']")
    #1.确定是否唯一
    print len(entrys)
    #2.确定使用的索引
    entry_idx = 0

    #分层，该用相对路径.//
    parts = entrys[entry_idx].find_elements_by_xpath(".//div[@class='TopicRelativeBoard-item']")
    #1.确定分层数
    print len(parts)

    #2.分层处理
    #2.1一层
    part_idx = 0
    #2.1.1获取分层内元素，使用相对路径.//
    nodes = parts[part_idx].find_elements_by_xpath(".//a[@class='TopicLink TopicTag']")
    print len(nodes)
    #2.1.2获取分层内元素的具体值
    for node in nodes:
        print node.text
        print node.get_attribute('href')

    #2.2二层
    #确定使用分层的索引
    part_idx = 1
    #2.2.1获取分层内元素，使用相对路径.//
    nodes = parts[part_idx].find_elements_by_xpath(".//a[@class='TopicLink TopicTag']")
    print len(nodes)
    #2.2.2获取分层内元素的具体值
    for node in nodes:
        print node.text
        print node.get_attribute('href')

    #完成，退出
    driver.quit()

if __name__ == '__main__':
    begin_url = "https://www.zhihu.com/topic/19551147/hot"
    #GetSearchContent(begin_url)
    getRelatedSinglePage(begin_url)
