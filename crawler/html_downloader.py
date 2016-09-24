# coding:utf-8
import urllib2


class HtmlDownloader(object):
    """
    HTML下载器
    """

    def download(self, url):
        """
        下载URL页面内容
        :param url:要下载的URL
        :return:URL页面的内容
        """

        # 跳过空URL
        if url is None:
            return None
        # 获取页面内容
        # TODO 根据页面结构扩展页面获取方法
        # urllib2模块提供网页下载功能
        response = urllib2.urlopen(url)
        # 返回码200表示请求成功
        if response.getcode() != 200:
            return None

        # 返回页面内容
        # read()返回网页的源码
        return response.read()
