# coding=utf-8

import time
from selenium import webdriver        
from selenium.webdriver.common.keys import Keys        
import selenium.webdriver.support.ui as ui        
from selenium.webdriver.common.action_chains import ActionChains

#先调用无界面浏览器PhantomJS或Firefox    
#driver = webdriver.PhantomJS()
driver = webdriver.Chrome()

def GetSearchContent(key):

    driver.get("http://fanyi.baidu.com/")

    #输入关键词并点击搜索
    guide_close = driver.find_element_by_xpath("//span[@class='app-guide-close']")
    guide_close.click()
    
    item_inp = driver.find_element_by_xpath("//textarea[@id='baidu_translate_input']")
    #item_inp.send_keys(key.decode('utf-8'))
    item_inp.send_keys(key)
    #wait the translate time
    time.sleep(1)
    res = driver.find_element_by_xpath("//div[@class='output-wrap output-blank']").text
    #print (res)
    driver.quit()
    return res

key = 'good man' 
print (GetSearchContent(key))
