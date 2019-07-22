## PM2.5_spider
### Crawling pm2.5 data from http://www.pm25.com, getting AQI of top 50 cities, and plotting result.
|版本|说明|
|:---|:---:|
|V1|遍历所有城市（350个左右）的网页，爬取城市名称、AQI和pm2.5，增加了程序运行时间的统计|
|V2|在一个页面上爬取所有城市的名词、省份、AQI、AQI排名和pm2.5（包括实时的、昨天的、一周的、一个月的）|

#### 可能的改进:
- V1的问题由于一次性处理的网页数量过多，需要的处理时间较长（分钟计，也可能因为超时而出现连接错误），考虑的办法是多线程/多进程
