arg=$1

case $arg in
    "ciku")
        #按照0-1000的索引获取搜狗词库
        mkdir data
        python ./sougou_ciku_spider_no_download_plus.py
        #所有的链接到data.all文件中
        cat data/* > data.all
        ;; #输出两个分号
    "cate")
        #根据抓取的词库信息，获取词库的类别信息，分类数据准备，具体词库在服务器存储，获取到底结果文件需要上传到服务器使用
        python ./sougou_get_all_links.py > category.dic
        #获取下载列表
        cat category.dic | awk -F "\t" '{print $1}' > download.list
        ;; #输出两个分号
    "down")
        #snownlp 分析文章和评论，测试文件，目前效果不好需要调优
        python ./snownlp_serve.py
        ;; #输出两个分号
    *)
        echo "error" 
        ;; #输出两个分号
esac
