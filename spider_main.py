# coding:utf-8
import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                
                # print(html_cont)
                new_urls, self_datas = self.parser.parse(new_url, html_cont) 
                # print (new_url)
                # print('craw %d : %s' % (count, new_url))
                self.urls.add_new_urls(new_urls)
                # print(new_urls)
                # print('mark')
                self.outputer.collect_data(self_datas)

                if count == 1:
                    break

                count = count + 1
            except:
                print('craw failed')

        self.outputer.output_html()


if __name__=='__main__':
    root_url = 'https://baike.baidu.com/historylist/%E9%83%AD%E6%96%87%E8%B4%B5/16550438'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
