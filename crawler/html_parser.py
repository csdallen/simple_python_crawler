# coding:utf-8
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):
    """
    HTML解析器
    """

    def parse(self, url, content):
        """
        解析URL页面内容
        :param url:页面URL
        :param content:页面的HTML代码
        :return:
        """

        # 跳过空页面
        if url is None or content is None:
            return
        # 设置要解析的内容(网页源码)、解析方式和内容编码，生成DOM树
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        # 页面中出现的新的URL和数据
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)

        return new_urls, new_data

    def _get_new_urls(self, url, soup):
        """
        获取URL页面中出现的新URL
        :param url:当前页面
        :param soup:BeautifulSoup
        :return:当前页面中出现的新URL的集合
        """

        # 存放新的URL的集合
        new_urls = set()

        # 根据正则表达式提取所有满足条件的URL
        # TODO 根据要爬取的网站的链接格式修改正则表达式和URL拼接方式
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        # 将短URL转换成完整URL，存入新URL集合
        for link in links:
            new_url = link['href']
            # 根据url格式拼接new_url
            new_full_url = urlparse.urljoin(url, new_url)
            new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(self, url, soup):
        """
        获取URL页面中出现的新数据
        :param url:当前页面
        :param soup:BeautifulSoup
        :return:页面中出现的新数据的集合
        """

        # 存放数据
        data = {}
        # 将页面URL放入数据中
        data['url'] = url

        # find()函数的使用文档：
        # https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#find-all
        # TODO 根据页面HTML格式修改数据提取方法
        # 百度百科结构：<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        # 提取标题
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title_node.get_text()
        # 百度百科结构：<div class="lemma-summary">
        # 提取摘要
        summary_node = soup.find('div', class_='lemma-summary')
        data['summary'] = summary_node.get_text()

        return data
