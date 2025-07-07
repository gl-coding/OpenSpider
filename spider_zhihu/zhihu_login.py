# coding=utf-8

import time
from selenium import webdriver        
from selenium.webdriver.common.keys import Keys        
import selenium.webdriver.support.ui as ui        
from selenium.webdriver.common.action_chains import ActionChains

#先调用无界面浏览器PhantomJS或Firefox    
#driver = webdriver.PhantomJS()
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.zhihu.com/")

print driver.get_cookies()

def GetSearchContent(key):

    #输入关键词并点击搜索
    #cookie = r'aliyungf_tc=AQAAACPlfFM4mwEATqmHPZcSd9Kx0KRf; q_c1=20b8290f701d44af839a038b480f352f|1508326257000|1508326257000; _xsrf=8ebb7c55f21ac0a2b09724e4b8c40ca9; r_cap_id="Njk1NDUwODdmNjE5NDBkNGJmMmEwZGU5ZjVhOGZkNDM=|1508326257|42306e00e442077c36090b630978889806494e9d"; cap_id="ZmFmZTY5ZWM1ODkwNDdiMGE1YmRiNTBkMzIxNDA4MGU=|1508326257|a0eacee3dc2d490312fba6d87eba448f48437726"; d_c0="AJDCDbrjiwyPTqiuC1QP60unnzfFL8DmnxU=|1508326259"; _zap=bad25d91-7b9d-4a30-8b4c-a901234fa6cf; l_n_c=1; z_c0=Mi4xN0FWQUFBQUFBQUFBa01JTnV1T0xEQmNBQUFCaEFsVk5nOGdPV2dBX3RpYXBaNlB5enFsZVZIZUNSNElXOUh2RUVR|1508326275|f0e40691486b23a70f1bf997bf64632c401e6fbc; __utma=51854390.234192105.1508326261.1508326261.1508326261.1; __utmb=51854390.0.10.1508326261; __utmc=51854390; __utmz=51854390.1508326261.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-1|2=registration_date=20140314=1^3=entry_date=20140314=1; _xsrf=8ebb7c55f21ac0a2b09724e4b8c40ca9'
    #driver.add_cookie({'value': cookie})
    driver.get("http://www.zhihu.com/")
    exit()
    signin = driver.find_element_by_xpath("//a[@href='#signin']")
    signin.click()
    password_sheet = driver.find_element_by_xpath("//span[@class='signin-switch-password']")
    password_sheet.click()
    account = driver.find_element_by_xpath("//input[@name='account']")
    account.send_keys("xxxxxxxxxxxx@qq.com")
    account = driver.find_element_by_xpath("//input[@name='password']")
    account.send_keys("xxxxxxxxxxxx")
    login_button = driver.find_element_by_xpath("//button[@class='sign-button submit']")
    login_button.click()
    time.sleep(3)
    exit()
    #item_inp.send_keys(key.decode('utf-8'))
    item_inp.send_keys(key)
    #wait the translate time
    time.sleep(0.5)
    res = driver.find_element_by_xpath("//div[@class='output-bd']").text
    #print (res)
    driver.quit()
    return res

key = 'good man' 
print (GetSearchContent(key))
