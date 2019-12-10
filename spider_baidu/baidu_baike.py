#coding=utf-8
from selenium import webdriver        
from selenium.webdriver.common.keys import Keys        

#初始化webdriver
driver = webdriver.Chrome()

def GetSearchContent(url, key):
    #打开指定url浏览器    
    driver.get(url)

    #输入关键词并点击搜索

    #1.找到输入框xpath路径
    item_inp = driver.find_element_by_xpath("//input[@id='query']")

    #2.输入关键词
    item_inp.send_keys(key)

    #3.点击回车直接搜索
    item_inp.send_keys(Keys.RETURN)
    
    driver.quit()

if __name__ == "__main__":
    url = "http://baike.baidu.com/"
    GetSearchContent(url, u"杨颖")
