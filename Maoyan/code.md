**总结**

```python
# 流程
1、创建项目 + 爬虫文件
2、items.py : 定义数据结构
3、spider.py: 解析数据
4、pipelines.py: 处理数据
5、setting.py : 全局配置
6、run.py : 运行爬虫
# respone的方法
1、response.xpath('')
2、response.text : 字符串
3、response.body : 字节串
# 选择器对象列表
1、xxx.xpath('').extract()
2、xxx.xpath('').extract_first()
3、xxx.xpath('').get()
# 重写start_requests()方法
1、去掉start_urls变量
2、def start_requests():
# settings.py中常用变量
1、LOG_LEVEL = ''
2、LOG_FILE = ''
3、FEED_EXPORT_ENCODING = ''
# 保存csv或json文件
1、scrapy crawl spider -o xxx.csv
# 存数据库
class xxxPipeline(object):
    def open_spider(self,spider):
        pass
    def process_item(self,item,spider):
        # 必须返回item
        return item
    def close_spider(self,spider):
        pass
```