#encoding=utf-8
from pymongo import MongoClient
import util3

def getCollection(dbname, collection):
	conn = MongoClient()
	colle = conn[dbname][collection]
	return colle

#getCollection("spider", "qiubai")

def dictToMongo(collection, dict):
	json_obj = util3.dictToJsonObj(dict)
	collection.insert(json_obj)