# Baidu_Baike_HistoryList_Demo
Crawl the users links and usernames in the history list of the entry

抓取词条历史版本页面的用户及用户页面链接

## How to run
`python spider_main.py`

## How to change the test link
Modify the root_url in the `spider_main.py`

```
if __name__=='__main__':
    root_url = 'https://baike.baidu.com/historylist/%E9%83%AD%E6%96%87%E8%B4%B5/16550438'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
```
