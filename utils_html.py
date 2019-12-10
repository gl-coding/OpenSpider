# coding=utf-8
import urllib 

def getHtml(url):  
    html = urllib.urlopen(url).read()  
    #print (html)
    return html  
  
def saveHtml(file_name, file_content):  
    with open(file_name, "wb") as f:  
        #写文件用bytes而不是str，所以要转码  
        f.write(file_content)  

if __name__ == "__main__":
    aurl = "https://baike.baidu.com/item/杨颖"  
    html = getHtml(aurl)  
    tar  = "data/baikedata.html"
    saveHtml(tar, html)  
  
    print("下载成功") 
