import os

BOT_NAME = "kickstarter"

SPIDER_MODULES = ["kickstarter.spiders"]
NEWSPIDER_MODULE = "kickstarter.spiders"

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0"

ROBOTSTXT_OBEY = True

RETRY_TIMES = 100

DOWNLOADER_MIDDLEWARES = {"scrapy_zyte_smartproxy.ZyteSmartProxyMiddleware": 610}
ZYTE_SMARTPROXY_ENABLED = True
ZYTE_SMARTPROXY_APIKEY = os.environ.get("ZYTE_SMARTPROXY_APIKEY")

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# HTTPCACHE_ENABLED = True
# HTTPCACHE_IGNORE_HTTP_CODES = [503, 504, 505, 500, 400, 401, 402, 403, 404]
