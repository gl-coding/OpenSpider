from selenium import webdriver
import platform 

#print platform.system()

def get_driver():
    system = platform.system()
    if system == "Linux":
        return webdriver.PhantomJS(executable_path='/home/ubuntu/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
    else:
        return webdriver.Chrome()
        #return webdriver.PhantomJS()

#driver = get_driver()
#driver.get("http://www.baidu.com")
#driver.close()
