# coding:utf-8


class UrlManager(object):
    """
    URL管理器
    """

    def __init__(self):
        # 使用set可以避免出现重复元素
        # 待处理的URL
        self.new_urls = set()
        # 已处理的URL
        self.old_urls = set()

    def add_new_url(self, url):
        """
        向URL管理器中添加一个URL
        :param root_url:
        :return:
        """

        # 过滤空的URL
        if url is None:
            return
        # 过滤已在待处理列表中的URL和已经处理过的URL
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """
        向URL管理器中添加多个URL
        :param new_urls:
        :return:
        """

        # 过滤空的URL列表
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        """
        判断URL管理器中是否还有待处理的URL
        :return:
        """

        # 如果待处理URL集合不为空，说明还有要处理的URL，返回True
        return len(self.new_urls) != 0

    def get_new_url(self):
        """
        从URL管理器中获取一个URL
        :return:
        """

        # 从待处理URL集合中取出一个URL并将其从集合中删除
        url = self.new_urls.pop()
        # 将该URL添加到已处理的URL集合中
        self.old_urls.add(url)
        return url
