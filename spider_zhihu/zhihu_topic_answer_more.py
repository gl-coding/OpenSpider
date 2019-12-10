# coding=utf-8

import time
from selenium import webdriver        

#先调用无界面浏览器PhantomJS或Firefox    
#driver = webdriver.PhantomJS()
driver = webdriver.Chrome()

def getRelatedSinglePage(url):
    driver.get(url)
    #歇两秒
    time.sleep(2)

    #找到入口xpath节点
    entrys = driver.find_elements_by_xpath("//div[@class='Card TopicFeedList']")
    #1.确定是否唯一
    print len(entrys)
    #2.确定使用的索引
    entry_idx = 0

    #分层，该用相对路径.//
    parts = entrys[entry_idx].find_elements_by_xpath(".//div[@class='List-item TopicFeedItem']")
    #1.确定分层数
    print len(parts)

    #2.分层处理（多层处理用for循环）
    for part in parts:
        #不需要指定索引，用的是find_elements，node不是list类型
        node = part.find_element_by_xpath(".//button[@class='Button ContentItem-more Button--plain']")
        node.click()
        time.sleep(1)

    #完成，退出
    #driver.quit()

if __name__ == '__main__':
    begin_url = "https://www.zhihu.com/topic/19563977/hot"
    getRelatedSinglePage(begin_url)
