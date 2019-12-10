#encoding=utf-8
import sys
import os
import time
import utils as ut
import json

#driver = webdriver.Chrome()
driver = ut.get_driver()

#num = sys.argv[1]
base = "https://pinyin.sogou.com/dict/cate/index/"
#url = "https://pinyin.sogou.com/dict/cate/index/1"
#url = sys.argv[1]
#url = "https://www.jianshu.com"

def test(url):
    driver.get(url)
    time.sleep(1)

    filename = url.replace("https://", "").replace("/", "_")
    filename = "data/" + filename

    if os.path.exists(filename):
        os.remove(filename)
    log = open(filename, "a+")

    cate = driver.find_element_by_xpath("//div[@class='cate_title']").text
    flag = cate.index(u"分类")
    cate_clean =  cate[1:flag-1]

    res_dic = {}
    arg_list = []
    while True:
        ciku_list = driver.find_elements_by_xpath("//div[@class='detail_title']")
        btn_list = driver.find_elements_by_xpath("//div[@class='dict_dl_btn']")
                #print len(ciku_list)
            #break
        length = len(ciku_list)
            #for ciku in ciku_list:
        for i in range(0, length):
                #print ciku.text
            name = ciku_list[i].text
            url = btn_list[i].find_element_by_xpath(".//a").get_attribute("href")
            arg_list.append({"name":name, "url":url})

        foot = driver.find_element_by_xpath("//div[@id='dict_page']")
        btns = foot.find_elements_by_xpath(".//li")
            #print len(btns)
        if len(btns) == 0:
                #print "============"
            break
        nextpage = btns[-1].text.strip()
          #print nextpage
        time.sleep(0.3)

        if nextpage == u"下一页":
            btns[-1].click()
        else:
            break
        time.sleep(0.5)

    res_dic[cate_clean] = arg_list
    json_data = json.dumps(res_dic)
    print >> log, json_data

if __name__ == "__main__":
    for i in range(1000):
        url = base + str(i)
        try:
            print url
            test(url)
            time.sleep(0.5)
        except:
            print "error"

