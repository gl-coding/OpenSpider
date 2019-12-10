import json

res_dic = {}

with open("data.all", "r") as f:
    for line in f:
        json_dic = json.loads(line.strip()) 
        for k, v in json_dic.items():
            #print k
            #continue
            for item in v:
                key = item["url"]
                val = item["name"] + ":" + k + ";"
                res_dic[key] = res_dic.get(key, "") + val
                #info = item["url"] + "\t" + item["name"] + "\t" + k
                #print info.encode("utf-8")

for k, v in res_dic.items():
    line = k + "\t" + v
    print line.encode("utf-8")
