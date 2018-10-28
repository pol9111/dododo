BOT_NAME = 'alqwe'

SPIDER_MODULES = ['alqwe.spiders']
NEWSPIDER_MODULE = 'alqwe.spiders'

ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False

DOWNLOAD_TIMEOUT = 180
DOWNLOAD_DELAY = 0

USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

DOWNLOADER_MIDDLEWARES = {
   'alqwe.middlewares.AliTaobaoproductAutoDownloaderMiddleware': 543,
}

ITEM_PIPELINES = {
   'alqwe.pipelines.AliTaobaoproductAutoPipeline': 300,
   'scrapy_redis.pipelines.RedisPipeline': 900,  # 数据保存到redis里
}


# 同时处理(每个response的)item的最大值。
CONCURRENT_ITEMS = 100
# 并发请求(concurrent requests)的最大值。
CONCURRENT_REQUESTS = 32



MONGO_URI = 'localhost'
MONGO_DATABASE = 'baidu'
MONGO_TABLE = 'video_info'

REDIS_URI = 'localhost'
REDIS_PORT = 6379
REDIS_PARAMS = {
    'db': 5
}



# 启用日志
LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_FILE = 'log'
LOG_LEVEL = 'DEBUG'
# 如果为 True ，进程所有的标准输出(及错误)将会被重定向到log中。例如， 执行 print 'hello' ，其将会在Scrapy log中显示。
LOG_STDOUT = False
# 当spider结束时dump Scrapy状态数据 (到Scrapy log中)。
STATS_DUMP = True
# spider完成爬取后发送Scrapy数据。
STATSMAILER_RCPTS = []




# scrapy-redis
# 使用了scrapy-redis里的去重组件，不使用scrapy默认的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用了scrapy-redis里的调度器组件，不使用scrapy默认的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 使用队列形式
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 允许暂停，redis请求记录不丢失
SCHEDULER_PERSIST = True



# scrapy-redis-bloomfilter
# 去重类，要使用Bloom Filter请替换DUPEFILTER_CLASS
DUPEFILTER_CLASS = "scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter"
# 散列函数的个数，默认为6，可以自行修改
BLOOMFILTER_HASH_NUMBER = 6
# Bloom Filter的bit参数，默认30，占用128MB空间，去重量级1亿
BLOOMFILTER_BIT = 30
# 使用了scrapy_redis_bloomfilter里的调度器组件，不使用scrapy默认的调度器
SCHEDULER = "scrapy_redis_bloomfilter.scheduler.Scheduler"
# 使用队列形式
SCHEDULER_QUEUE_CLASS = "scrapy_redis_bloomfilter.queue.SpiderQueue"
# 允许暂停，redis请求记录不丢失
SCHEDULER_PERSIST = True





PROXIES = [
  {'ip_port': '111.11.228.75:80', 'password': ''},
]





# 启动下载文件
ITEM_PIPELINES = {
    'scrapy.pipelines.files.FilesPipeline': 1,
}

# 文件保存目录
FILES_STORE = 'examples_src'


# 启动下载图片
ITEM_PIPELINES = {
'scrapy.pipelines.images.ImagesPipeline': 1,
}

# 图片保存目录
IMAGES_STORE = 'download_images'

#下面有个图片全的






# 不常用

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.robotstxt.RobotsTxtMiddleware': 100,
    'scrapy.contrib.downloadermiddleware.httpauth.HttpAuthMiddleware': 300,
    'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware': 350,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 400,
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 500,
    'scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware': 550,
    'scrapy.contrib.downloadermiddleware.redirect.MetaRefreshMiddleware': 580,
    'scrapy.contrib.downloadermiddleware.httpcompression.HttpCompressionMiddleware': 590,
    'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': 600,
    'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 700,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 750,
    'scrapy.contrib.downloadermiddleware.chunked.ChunkedTransferMiddleware': 830,
    'scrapy.contrib.downloadermiddleware.stats.DownloaderStats': 850,
    'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 900,
}


# spider中间件
SPIDER_MIDDLEWARES = {
    'scrapy.contrib.spidermiddleware.httperror.HttpErrorMiddleware': 50,
    'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': 500,
    'scrapy.contrib.spidermiddleware.referer.RefererMiddleware': 700,
    'scrapy.contrib.spidermiddleware.urllength.UrlLengthMiddleware': 800,
    'scrapy.contrib.spidermiddleware.depth.DepthMiddleware': 900,
}



# 保存项目中启用的插件及其顺序的字典。
EXTENSIONS_BASE = {
    'scrapy.contrib.corestats.CoreStats': 0,
    'scrapy.telnet.TelnetConsole': 0,
    'scrapy.contrib.memusage.MemoryUsage': 0,
    'scrapy.contrib.memdebug.MemoryDebugger': 0,
    'scrapy.contrib.closespider.CloseSpider': 0,
    'scrapy.contrib.feedexport.FeedExporter': 0,
    'scrapy.contrib.logstats.LogStats': 0,
    'scrapy.contrib.spiderstate.SpiderState': 0,
    'scrapy.contrib.throttle.AutoThrottle': 0,
}




# 导出文件路径。
FEED_URI = 'export_data/%(name)s.data'
# 导出数据格式。
FEED_FORMAT = 'csv'
# 导出文件编码（默认情况下json文件使用数字编码，其他使用utf-8编码）。
FEED_EXPORT_ENCODING = 'gbk'
# 导出数据包含的字段（默认情况下导出所有字段），并指定次序。
FEED_EXPORT_FIELDS = ['name', 'author', 'price']
# 用户自定义Exporter字典，添加新的导出数据格式时使用。
FEED_EXPORTERS = {'excel': 'my_project.my_exporters.ExcelItemExporter




# 默认每个域名的并发数：8
CONCURRENT_REQUESTS_PER_DOMAIN = 8
# 每个IP的最大并发数：0表示忽略
CONCURRENT_REQUESTS_PER_IP = 0




# 图片保存
ITEM_PIPELINES = { 'top250.pipelines.Top250Pipeline': 1,}
IMAGES_STORE = 'images'   #存储图片的文件夹位置
IMAGES_EXPIRES = 90 # 图像管道避免下载最近已经下载的图片。使用 IMAGES_EXPIRES 设置可以调整失效期限
# 最小宽高
IMAGES_MIN_HEIGHT = 110
IMAGES_MIN_WIDTH = 110
# 缩略图
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}




# 爬取URL的最大长度
URLLENGTH_LIMIT = 2083




# 若 DOWNLOAD_DELAY 为0(默认值)，该选项将不起作用。Scrapy将会等待一个随机的值 (0.5到1.5之间的一个随机值
RANDOMIZE_DOWNLOAD_DELAY = True




# 定义request允许重定向的最大次数。超过该限制后该request直接返回获取到的结果。
REDIRECT_MAX_TIMES = 20
# 限制自动重定向到最大延迟(秒)。
REDIRECT_MAX_METAREFRESH_DELAY = 100
# 修改重定向请求相对于原始请求的优先级。 负数意味着更多优先级。
REDIRECT_PRIORITY_ADJUST = +2




# 表明 telnet 终端 (及其插件)是否启用的布尔值。
TELNETCONSOLE_ENABLED = True
# telnet终端使用的端口范围。如果设置为 None 或 0 ， 则使用动态分配的端口。
TELNETCONSOLE_PORT = [6023, 6073]





# 是否启用内存调试。
MEMDEBUG_ENABLED = False
# 如果该设置不为空，当启用内存调试时将会发送一份内存报告到指定的地址；否则该报告将写到log中。
MEMDEBUG_NOTIFY = ['user@example.com']


# 是否启用内存使用插件。当Scrapy进程占用的内存超出限制时，该插件将会关闭Scrapy进程， 同时发送email进行通知。
MEMUSAGE_ENABLED = False
# 在发送警告email前所允许的最大内存数(单位: MB)(如果 MEMUSAGE_ENABLED为True)。 如果为0，将不发送警告。
MEMUSAGE_WARNING_MB = 0
# 在关闭Scrapy之前所允许的最大内存数(单位: MB)(如果 MEMUSAGE_ENABLED为True)。 如果为0，将不做限制。
MEMUSAGE_LIMIT_MB = 0
# 每个spider被关闭时是否发送内存使用报告。
MEMUSAGE_REPORT = False
# 达到内存限制时通知的email列表。
MEMUSAGE_NOTIFY_MAIL = ['user@example.com']






# 整数值。用于根据深度调整request优先级。如果为0，则不根据深度进行优先级调整。
DEPTH_PRIORITY = 0
# 爬取网站最大允许的深度(depth)值。如果为0，则没有限制。
DEPTH_LIMIT = 0
# 是否收集最大深度数据。
DEPTH_STATS = True
# 是否收集详细的深度数据。如果启用，每个深度的请求数将会被收集在数据中。
DEPTH_STATS_VERBOSE = False

# 广度优先顺序
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'



# Enable and configure the AutoThrottle extension (disabled by default)
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

# 缓存
# HTTPCACHE_ENABLED = True # 打开缓存
#HTTPCACHE_EXPIRATION_SECS = 0 # 设置缓存过期时间（单位：秒）
#HTTPCACHE_DIR = 'httpcache' # 缓存路径(默认为：.scrapy/httpcache)
#HTTPCACHE_IGNORE_HTTP_CODES = [] # 忽略的状态码
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage' # 缓存模式(文件缓存)