arg=$1

case $arg in
    "ciku_dl")
        #下载搜狗词库
        #bash download.sh 1 100
        #bash download.sh 101 1000
        #bash download.sh 1001 10000
        #bash download.sh 10001 20000
        #bash download.sh 20001 30000
        bash download.sh 30001 38146
        ;; #输出两个分号
    "ciku_dl")
        #搜狗词库转换为普通编码，map.dic 转化映射日志
        bash ./sougou_scel_convert.sh
        ;; #输出两个分号
    *) 
        echo "error" 
        ;; #输出两个分号 
esac
