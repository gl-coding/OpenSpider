#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
OpenSpider示例脚本
演示如何使用项目中的不同爬虫模块
"""

import os
import sys
import time

# 将项目根目录添加到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def example_baidu_baike():
    """百度百科爬虫示例"""
    from spider_baidu.baidu_baike import GetSearchContent
    print("正在爬取百度百科内容...")
    result = GetSearchContent("https://baike.baidu.com/", "人工智能")
    print("爬取完成!")

def example_baidu_fanyi():
    """百度翻译爬虫示例"""
    from spider_baidu.baidu_fanyi import GetSearchContent
    print("正在翻译文本...")
    result = GetSearchContent("Hello, world!")
    print("翻译结果:", result)

def example_weibo_search():
    """微博搜索爬虫示例"""
    from spider_weibo.weibo_search import GetSearchContent
    print("正在搜索微博内容...")
    GetSearchContent("人工智能")
    print("搜索完成!")

def example_zhihu_question():
    """知乎问题爬虫示例"""
    from spider_zhihu.zhihu_question import getRelatedSinglePage
    print("正在爬取知乎问题相关内容...")
    getRelatedSinglePage("https://www.zhihu.com/question/35903519")
    print("爬取完成!")

def example_sougou_ciku():
    """搜狗词库爬虫示例"""
    import spider_sougou.sougou_ciku_spider_no_download_plus as sougou
    print("正在爬取搜狗词库...")
    sougou.test("https://pinyin.sogou.com/dict/cate/index/1")
    print("爬取完成!")

if __name__ == "__main__":
    print("OpenSpider示例脚本")
    print("=" * 50)
    
    print("\n1. 百度百科爬虫")
    # example_baidu_baike()  # 取消注释以运行示例
    
    print("\n2. 百度翻译爬虫")
    # example_baidu_fanyi()  # 取消注释以运行示例
    
    print("\n3. 微博搜索爬虫")
    # example_weibo_search()  # 取消注释以运行示例
    
    print("\n4. 知乎问题爬虫")
    # example_zhihu_question()  # 取消注释以运行示例
    
    print("\n5. 搜狗词库爬虫")
    # example_sougou_ciku()  # 取消注释以运行示例
    
    print("\n请取消注释选择要运行的示例")
    print("=" * 50) 