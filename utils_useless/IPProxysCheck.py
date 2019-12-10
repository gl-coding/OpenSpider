#encoding="utf-8"
import urllib2
import util
import urllib
from selenium import webdriver
from selenium.webdriver.common.proxy import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def test():
    proxy_support = urllib2.ProxyHandler({'http':'http://61.187.251.235:80'}) 
    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler) 
    urllib2.install_opener(opener) 
    content = urllib2.urlopen('http://180.76.247.130:8888/').read()

    util.saveFile("ipcheck.html", content)

def testChinese():
    key = "hh"
    urllib.parse.urlencode(key)

def testDriverFireFox():

    myProxy = "86.111.144.194:3128"
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': myProxy,
        'ftpProxy': myProxy,
        'sslProxy': myProxy,
        'noProxy':''})

    driver = webdriver.Firefox(proxy=proxy)
    driver.set_page_load_timeout(30)
    # driver.get('http://180.76.247.130:888/')
    driver.get('http://www.baidu.com')

def testDriverChrome():
    profile = webdriver.FirefoxProfile() 
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", "60.2.148.253")
    profile.set_preference("network.proxy.http_port", 80)
    profile.update_preferences() 
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get("http://icanhazip.com")
    # print driver.find_element_by_xpath("//div[@id='u1']").text

def testPhantomJs():
    from selenium.webdriver.common.proxy import *
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    phantomjs_path = r"C:\Python36-32\Scripts\phantomjs.exe"
    service_args = [
        '--proxy=61.187.251.235:80',
        '--proxy-type=https',
        ]
    driver = webdriver.PhantomJS(executable_path=phantomjs_path,service_args=service_args)
    driver.get("https://www.baidu.com")
    print driver.page_source.encode('utf-8')
    print "="*70
    print driver.title
    driver.save_screenshot(r"d:\test.png")
    driver.quit()

def getMyIP():
    from selenium import webdriver
    phantomjs_path = r"C:\Python36-32\Scripts\phantomjs.exe"
    service_args = ['--proxy=111.62.251.66:80', '--proxy-type=http']
    driver = webdriver.PhantomJS(service_args=service_args)
    # driver = webdriver.PhantomJS()
    driver.get("http://icanhazip.com")
    print (driver.page_source)
    driver.close()

if __name__ == "__main__":
    # test()
    # testChinese()
    # testDriverFireFox()
    testDriverChrome()
    # testPhantomJs()
    # getMyIP()