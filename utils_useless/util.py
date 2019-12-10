# coding=utf-8
import random
import jieba.posseg as pseg
import json
import os
import time
from functools import wraps
import logging

def saveFile(file_name, file_content):
    #    注意windows文件命名的禁用符，比如 / 
    with open(file_name.replace('/', '_'), "wb") as f:  
        #   写文件用bytes而不是str，所以要转码  
        f.write(file_content)

def removeFile(file_name):
	if os.path.exists(file_name):
		os.remove(file_name)

def codeprocess(src):
	mychar = chardet.detect(src) 
	bianma = mychar['encoding'].lower()
	print (bianma)
	res = src.decode(bianma,'ignore').encode("utf-8")
	return res

def genRandomTimeInterval():
	return random.randint(1,3)

def shuffleSetenceByChar(setence):
	char_list = list(setence)
	#print char_list
	return
	result = pseg.cut(setence)
	word_list = []
	for w in result:
		word_list.append(w.word)
	#print word_list
	shuffle_list = random.shuffle(word_list)
	#print shuffle_list

def shuffleSetenceByWord(setence):
	result = pseg.cut(setence)
	word_list = []
	for w in result:
		word_list.append(w.word)
	#print word_list
	shuffle_list = random.shuffle(word_list)
	#print shuffle_list

#shuffleSetenceByWord("小明硕士毕业于中国科学院计算所，后在日本的京都大学深造")

def dictToJsonObj(dict):
	json_str = json.dumps(dict).strip()
	json_obj = json.loads(json_str)
	return json_obj

def cleanString(string):
	return string.strip()

def cleanFileContent(inputfile):
	timestamp = str(time.time()).replace(".", "_")
	outputfile = timestamp + ".tmp"
	with open(outputfile, 'w') as w:
		with open(inputfile, 'r') as r:
			for line in r:
				if len(line) < 2:
					continue
				w.write(line)
	os.remove(inputfile)
	os.rename(outputfile, inputfile)

#cleanFile("side-content.txt")

def getRuntime(function):
	@wraps(function) 
	def function_timer(*args, **kwargs):
		t0 = time.time() 
		result = function(*args, **kwargs) 
		t1 = time.time() 
		print ("Total time running %s: %s seconds" % (function, str(t1-t0)) ) 
		return result 
	return function_timer

#@getRuntime
#def mysum(n):
#	return sum([i for i in range(n)])
#print (mysum(1000000))

def loggingTest():
	#logging.debug('This is debug message')
	#logging.info('This is info message')
	#logging.warning('This is warning message')

	logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log', # output file
                filemode='w') # "w" or "a"

	logging.debug('This is debug message')
	logging.info('This is info message')
	logging.warning('This is warning message')

#loggingTest()

def loggingWindownAndFile():
	# 第一步，创建一个logger
	logger = logging.getLogger()
	logger.setLevel(logging.INFO)    # Log等级总开关

	# 第二步，创建一个handler，用于写入日志文件
	logfile = '.\logger.txt'
	fh = logging.FileHandler(logfile, mode='w')
	fh.setLevel(logging.DEBUG)   # 输出到file的log等级的开关
	# 第三步，再创建一个handler，用于输出到控制台
	ch = logging.StreamHandler()
	ch.setLevel(logging.WARNING)   # 输出到console的log等级的开关

	# 第四步，定义handler的输出格式
	formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
	fh.setFormatter(formatter)
	ch.setFormatter(formatter)

	# 第五步，将logger添加到handler里面
	logger.addHandler(fh)
	logger.addHandler(ch)

	# 日志
	logger.debug('this is a logger debug message')
	logger.info('this is a logger info message')
	logger.warning('this is a logger warning message')
	logger.error('this is a logger error message')
	logger.critical('this is a logger critical message')

#loggingWindownAndFile()