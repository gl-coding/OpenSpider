import redis

newUrl_set = "newurl_set"
oldUrl_set = "oldurl_set"
urlContent_dict = "urlcontent_dict"

rc = redis.Redis(host = "127.0.0.1", port = 6379)

def cleanRedis():
	rc.delete(newUrl_set)
	rc.delete(oldUrl_set)
	rc.delete(urlContent_dict)

def kvToRedis(k, v):
	if rc.hexists(urlContent_dict, k):
		return
	dic = {
		k : v
	}
	rc.hmset(urlContent_dict, dic)

def getDict():
	for k, v in rc.hgetall(urlContent_dict).items():
		print (str(v, encoding = "utf-8"))

def addsvToNewUrlSet(value):
	rc.sadd(newUrl_set, value)

def moveNewToOld(value):
	rc.smove(newUrl_set, oldUrl_set, value)

def existsInOld(value):
	return rc.sismember(oldUrl_set, value)

def returnRandNewItem():
	return rc.srandmember(newUrl_set)

if __name__ == '__main__':
	getDict()
	exit()
	cleanRedis()
	kvToRedis("url", "name")
	print (rc.hget(urlContent_dict, "url"))
	addsvToNewUrlSet("ok")
	moveNewToOld("ok")
	print(existsInOld("ok"))