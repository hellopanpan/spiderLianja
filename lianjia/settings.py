# -*- coding: utf-8 -*-

# Scrapy settings for lianjia project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lianjia'

SPIDER_MODULES = ['lianjia.spiders']
NEWSPIDER_MODULE = 'lianjia.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lianjia (+http://www.yourdomain.com)'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
	'Cookie': 'lianjia_uuid=c5f42ed9-e135-4516-a763-c79d2a9d991a; gr_user_id=f75e30f4-6c47-4658-86d8-9bea24563bee; UM_distinctid=15dc05f79dbf9-039339b0230015-36624308-1fa400-15dc05f79dcb73; _jzqx=1.1509677987.1509677987.1.jzqsr=google%2Eco%2Ejp|jzqct=/.-; _smt_uid=59894fbc.58b696e0; _ga=GA1.2.575432985.1502171071; select_city=510100; _jzqckmp=1; _gid=GA1.2.1430153374.1514515777; gr_session_id_a1a50f141657a94e=c8d8be9e-21d2-4edb-9b84-d4c0a7f828dc; CNZZDATA1253492306=437679023-1502169617-https%253A%252F%252Fwww.baidu.com%252F%7C1514523902; CNZZDATA1255633284=825603553-1502169476-https%253A%252F%252Fwww.baidu.com%252F%7C1514523138; all-lj=fa25c352c963a53c37faa70f46a58187; lianjia_ssid=af76f7ad-8b23-4118-b2ec-aaa3b565ca08; _qzjc=1; _jzqa=1.479832818372744500.1502171069.1514525937.1514526143.7; _jzqc=1; _jzqy=1.1502171069.1514526143.2.jzqsr=baidu|jzqct=%E8%87%AA%E5%A6%82%E5%8F%8B%E5%AE%B6.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6; CNZZDATA1254525948=2134451337-1502168494-https%253A%252F%252Fwww.baidu.com%252F%7C1514526107; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1514515769,1514517166,1514525937,1514526143; _qzja=1.337731773.1502171068909.1514525937101.1514526143053.1514526162800.1514526657211.0.0.0.70.7; _qzjb=1.1514525937100.8.0.0.0; _qzjto=32.4.0; _jzqb=1.3.10.1514526143.1; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1514526657; CNZZDATA1255604082=1169639326-1502165809-https%253A%252F%252Fwww.baidu.com%252F%7C1514526399',
	'Referer': 'https://cd.lianjia.com/ershoufang/'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lianjia.middlewares.LianjiaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'lianjia.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
	'lianjia.pipelines.LianjiaPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
