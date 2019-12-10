#encoding=utf-8
from pymongo import MongoClient
import xlwt
import time

import emotionAnalyse as ea
import util3

global row
global outfile
global sheet

#在添加每一个sheet之后，初始化字段

def initXLS(filename, title_list):
    
    global row
    global outfile
    global sheet

    sheetName = str(time.time()).replace(".", "_")
    outfile = xlwt.Workbook(encoding = 'utf-8')
    sheet = outfile.add_sheet(sheetName)

    row  = 0
    for i in range(len(title_list)):
        sheet.write(row, i, title_list[i])
    row = row + 1
    outfile.save(filename)

#将一条list的内容写入excel
def writeXLS(filename, content_list):
    global row
    global outfile
    global sheet

    for i in range(len(content_list)):
    	print (content_list[i])
    	# content = util3.byteToUTFStr(content_list[i])
    	content = content_list[i]
    	sheet.write(row, i, content)
    row = row + 1
    outfile.save(filename)

def getCollectionKeys(dbname, collection):
	res = []
	conn = MongoClient()
	collection_json = conn[dbname][collection]
	for json_obj in collection_json.find():
		for k in json_obj.keys():
			res.append(k)
		break
	if len(res) == 0:
		return res
	res.remove('_id')
	# conn.close()
	#print res
	return res

#print getCollectionKeys("spider", "qiubai")

def scanMongodb(dbname, collection):
	conn = MongoClient()
	qiubai = conn[dbname][collection]
	#qiubai = db.qiubai
	#print db.collection_names()
	#qiubai.insert({"test": "ok"})
	#qiubai.remove()
	for json_obj in qiubai.find():
		print (json_obj["content"])
	conn.close()

#scanMongodb("spider", "qiubai")
#exit()

def processMongoData(dbname, collection, analyse_seg):
	# dbname = "spider"
	# collection = "qiubai"
	result_file = dbname + "_" + collection + ".xls"
	#title_list = ['博主昵称', '博主主页', '微博认证']
	dbTitle_list = getCollectionKeys(dbname, collection)
	#print (dbTitle_list)
	analyseContentTitle_list = ea.getTitleList()
	#print (analyseContentTitle_list)
	title_list = dbTitle_list + analyseContentTitle_list
	#print (title_list)
	#print title_list
	#return
	initXLS(result_file, title_list)

	conn = MongoClient()
	db = conn[dbname][collection]
	#count = 0
	for json_obj in db.find():
		write_list = []
		#write_list = json_obj.values()
		for t in dbTitle_list:
			#print t
			write_list.append(json_obj[t])
		#count += 1
		# author = json_obj["author"]
		# like = json_obj["like"]
		# write_list.append(author)
		# write_list.append(like)
		# write_list.append(content)
		if analyse_seg != "":
			content = json_obj[analyse_seg]
			analyse_list = ea.analyseContent(content, printFlag=False)
			write_list.extend(analyse_list)
		#print write_list
		writeXLS(result_file, write_list)
		# if count == 1:
		# 	break

	# content_list = ['a', 'b', 'c']
	# writeXLS(filename, content_list)
	# writeXLS(filename, content_list)
	# writeXLS(filename, content_list)

if __name__ == "__main__":
	#processMongoData("spider", "qiubai", "content")
	processMongoData("spider", "hotweibo", "")