# OpenSpider - 多平台网络爬虫工具集

OpenSpider是一个综合性的网络爬虫工具集，支持多个中文互联网平台的数据采集，包括百度、微博、知乎、微信、搜狗等。

## 项目结构

```
OpenSpider/
  - spider_baidu/       # 百度相关爬虫
  - spider_douban/      # 豆瓣相关爬虫
  - spider_sougou/      # 搜狗相关爬虫
  - spider_weibo/       # 微博相关爬虫
  - spider_weixin/      # 微信相关爬虫
  - spider_zhihu/       # 知乎相关爬虫
  - utils_*.py          # 通用工具类
  - utils_useless/      # 不常用的工具类
```

## 功能模块

### 百度爬虫
- `baidu_baike.py`: 爬取百度百科内容
- `baidu_fanyi.py`: 爬取百度翻译结果

### 微博爬虫
- `weibo_hot.py`: 获取微博热搜榜
- `weibo_hot_soup.py`: 使用BeautifulSoup解析微博热搜
- `weibo_login.py`: 模拟微博登录
- `weibo_mainpage.py`: 爬取微博主页内容
- `weibo_search.py`: 搜索微博内容，支持高级搜索和时间限定
- `weibo_user.py`: 爬取微博用户信息

### 知乎爬虫
- `zhihu_login.py`: 模拟知乎登录
- `zhihu_question.py`: 爬取知乎问题内容
- `zhihu_relatedquestion.py`: 爬取知乎相关问题
- `zhihu_search.py`: 搜索知乎内容
- `zhihu_topic.py`: 爬取知乎话题内容
- `zhihu_topic_answer_more.py`: 爬取知乎话题下的更多回答
- `zhihu_topic_content_more.py`: 爬取知乎话题下的更多内容

### 微信爬虫
- `weixin.py`: 微信公众号内容爬取
- `weixin_search.py`: 搜索微信公众号内容

### 搜狗爬虫
- `sougou_ciku_spider_no_download_plus.py`: 爬取搜狗输入法词库
- `sougou_get_all_links.py`: 获取搜狗词库下载链接
- `sougou_scel_convert.py`: 转换搜狗词库格式(.scel)为文本格式
- 其他脚本: 包括下载和转换的批处理脚本

### 豆瓣爬虫
- `douban.py`: 爬取豆瓣内容

## 工具类

- `utils_driver.py`: Selenium驱动工具，根据不同操作系统返回适合的WebDriver
- `utils_html.py`: HTML处理工具
- `utils_image.py`: 图片处理工具
- `utils_net.py`: 网络请求工具，包含代理IP和User-Agent管理

## 技术特点

1. 使用Selenium模拟浏览器行为，支持Chrome和PhantomJS
2. 采用XPath和BeautifulSoup解析页面内容
3. 支持代理IP切换，避免IP被封
4. 支持多种数据存储格式，包括文本、Excel等
5. 提供多种爬取策略，包括定时爬取、增量爬取等

## 环境要求

- Python 2.7
- Selenium
- BeautifulSoup
- lxml
- Chrome浏览器或PhantomJS
- 其他依赖库(requirements.txt待添加)

## 使用说明

各个爬虫模块可以单独使用，根据需要选择相应的脚本运行。例如：

```bash
# 爬取微博搜索结果
python spider_weibo/weibo_search.py

# 爬取知乎问题
python spider_zhihu/zhihu_question.py

# 爬取搜狗词库
python spider_sougou/sougou_ciku_spider_no_download_plus.py
```

## 注意事项

1. 请遵守网站的robots协议
2. 控制爬取频率，避免对目标网站造成压力
3. 获取的数据请勿用于商业用途
4. 部分爬虫需要登录账号，请自行配置账号信息

## 免责声明

本项目仅供学习和研究使用，请勿用于非法用途。使用本项目所产生的一切后果由使用者自行承担。 