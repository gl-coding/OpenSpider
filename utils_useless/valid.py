# coding=utf-8
#python2.7
import urllib2
import urllib
import util
from bs4 import BeautifulSoup
import re
from pprint import pprint
import time
import json
from pymongo import MongoClient
import pytesseract
from PIL import Image,ImageEnhance

url = "http://s.weibo.com/ajax/pincode/pin?type=sass&ts=1508411223"
User_Agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
req = urllib2.Request(url)
req.add_header('User-Agent',User_Agent)

response = urllib2.urlopen(req, timeout=5)
data = response.read()
util.saveFile('test.jpg', data)


image = Image.open('./test.jpg')
imgry = image.convert('L')#图像加强，二值化
sharpness =ImageEnhance.Contrast(imgry)#对比度增强
sharp_img = sharpness.enhance(2.0)
vcode = pytesseract.image_to_string(image)

print (vcode)