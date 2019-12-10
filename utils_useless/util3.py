import json
import configparser
import os

def dictToJsonObj(dict):
	json_str = json.dumps(dict).strip()
	json_obj = json.loads(json_str)
	return json_obj

globalConfigFile = "curDoingHotKey.config"
globalSection = "curHotKey"

def writeConfig(key, value):
	configfile = globalConfigFile
	cf = configparser.ConfigParser()
	# add section / set option & key
	section = globalSection
	cf.add_section(section)
	cf.set(section, key, value)

	with open(configfile,"w") as f:
	    cf.write(f)

#writeConfig("key", "chenguanxi")

def readConfig(key):
	configfile = globalConfigFile
	section = globalSection
	cf = configparser.ConfigParser()
	cf.read(configfile)
	v = cf.get(section, key)
	#print (v)
	return v

def byteToUTFStr(bytestr):
	return str(bytestr, encoding = "utf-8")

#v = readConfig("key")
#print (v)