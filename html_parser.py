# coding:utf-8
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
from urllib.parse import quote


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()

        # links = soup.find_all('a', href=re.compile(r'/view/[\u4e00-\u9fa5]+'))
        links = soup.find_all('a',href=re.compile(r'www.baidu.com/p/*'))
        title_nodes = soup.find_all('a', class_='uname')		
        reason_nodes = soup.find_all('td', class_='reason')
        self_datas = []
        ii =0
        i = len(links)   
        while (ii<i):
            res_data = {}
            new_url = links[ii]['href']
            new_full_url = new_url
            new_urls.add(new_full_url)
            res_data['url'] = new_url
            res_data['title'] = title_nodes[ii].get_text()
            # print(res_data['url'])
            res_data['summary'] = reason_nodes[ii].get_text()
            ii = ii+1
            self_datas.append(res_data)
        
        # print(ii)
        return new_urls, self_datas

    def _get_new_data(self, page_url, soup):
        res_data = {}
        # url
        res_data['url'] = page_url
        title_node = soup.find('a', class_='uname')
        res_data['title'] = title_node.get_text()
        summary_node = soup.find('td', class_='reason')
        res_data['summary'] = summary_node.get_text()
        # print(res_data)
        return res_data

    def parse(self, page_url, html_cont):
        # print(page_url)
        # print('----')
        # print(html_cont)
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        # print(soup.prettify())
        new_urls, self_datas = self._get_new_urls(page_url, soup)
        # print('mark')
        return new_urls, self_datas