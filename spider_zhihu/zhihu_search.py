# coding=utf-8

import time
from selenium import webdriver        
from selenium.webdriver.common.keys import Keys        
import selenium.webdriver.support.ui as ui        
from selenium.webdriver.common.action_chains import ActionChains

#先调用无界面浏览器PhantomJS或Firefox    
#driver = webdriver.PhantomJS()
driver = webdriver.Chrome()

#拼接url直接打开链接
def searchByUrl(url):
    driver.get(url)
    time.sleep(2)
    driver.quit()


if __name__ == "__main__":
    key = '故事' 
    url = "https://www.zhihu.com/search?type=content&q=" + key
    searchByUrl(key)
