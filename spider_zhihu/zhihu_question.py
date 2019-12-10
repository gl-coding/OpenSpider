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
    entrys = driver.find_elements_by_xpath("//div[@class='Card-section SimilarQuestions-list']")
    #1.确定是否唯一
    print len(entrys)
    #2.确定使用的索引
    entry_idx = 0

    #分层，该用相对路径.//
    parts = entrys[entry_idx].find_elements_by_xpath(".//div[@class='SimilarQuestions-item']")
    #1.确定分层数
    print len(parts)

    #2.分层处理（多层处理用for循环）
    for part in parts:
        #只有一个元素的时候，需要指定索引，因为node类型为list，用的是find_elements
        #node = part.find_elements_by_xpath(".//a")
        #print node[0].get_attribute('href')

        #不需要指定索引，用的是find_elements，node不是list类型
        node = part.find_element_by_xpath(".//a")
        print node.get_attribute('href')
        print node.text

    #完成，退出
    driver.quit()

if __name__ == '__main__':
    begin_url = "https://www.zhihu.com/question/35903519"
    getRelatedSinglePage(begin_url)
