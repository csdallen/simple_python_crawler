# coding:utf-8
from crawler import html_downloader
from crawler import html_outputer
from crawler import html_parser
from crawler import url_manager


class CrawlerMain:
    """
    爬虫总调度程序
    """

    def __init__(self):
        # URL管理器
        self.manager = url_manager.UrlManager()
        # HTML下载器
        self.downloader = html_downloader.HtmlDownloader()
        # HTML解析器
        self.parser = html_parser.HtmlParser()
        # HTML输出器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        """
        爬虫调度函数
        :param root_url:入口URL
        :return:
        """

        # 记录当前在抓取第几个URL
        count = 1

        # 将入口URL加入URL管理器
        self.manager.add_new_url(root_url)
        # URL管理器中有URL时，一直执行
        while self.manager.has_new_url():
            try:
                # 获取URL
                new_url = self.manager.get_new_url()
                # 输出当前打印的URL的序号和地址
                print 'crawl url %d : %s.' % (count, new_url)
                # 下载URL页面
                html_content = self.downloader.download(new_url)
                # 解析URL页面
                new_urls, new_data = self.parser.parse(new_url, html_content)
                # 将新的URL加入URL管理器
                self.manager.add_new_urls(new_urls)
                # 收集数据
                self.outputer.collect_data(new_data)
                # 爬取足够数量的数据后结束爬取
                if count == 100:
                    break
                count += 1
            except:
                # 出现异常，爬取URL数据失败
                print 'crawl failed.'
        # 输出收集到的数据
        self.outputer.output_html()


if __name__ == '__main__':
    # 入口URL
    root_url = 'http://baike.baidu.com/view/21087.htm'
    # 爬虫对象
    obj_crawler = CrawlerMain()
    # 启动爬虫
    obj_crawler.craw(root_url)
