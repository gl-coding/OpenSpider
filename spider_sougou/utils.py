from selenium import webdriver
import platform 

#print platform.system()

def get_driver():
    system = platform.system()
    if system == "Linux":
        return webdriver.PhantomJS()
    else:
        return webdriver.Chrome()
        #return webdriver.PhantomJS()

#driver = get_driver()
#driver.get("http://www.baidu.com")
#driver.close()
