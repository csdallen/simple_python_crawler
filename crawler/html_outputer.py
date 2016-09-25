# coding:utf-8


class HtmlOutputer(object):
    """
    HTML输出器
    """

    def __init__(self):
        # 用于维护数据的列表
        self.data_list = []

    def collect_data(self, data):
        """
        收集数据
        :param data:需要收集的数据
        """

        # 过滤空数据
        if data is None:
            return
        self.data_list.append(data)

    def output_html(self):
        """
        将收集到的数据写出到HTML文件中
        """

        # 将数据输出到文件，完成后自动关闭文件
        with open('output.html', 'w') as f_out:
            # 写HTML开头
            # 网页meta应声明为"UTF-8"，否则某些系统的浏览器默认按gbk编码读取
            f_out.write('''
                <html>
                <head>
                <meta charset=""UTF-8"">
                <head>
                <body>
                <table>
            ''')
            # 写数据
            for data in self.data_list:
                # 默认编码方式未ASCII
                f_out.write('<tr>')
                f_out.write('<td>%s</td>' % data['url'].encode('utf-8'))
                f_out.write('<td>%s</td>' % data['title'].encode('utf-8'))
                f_out.write('<td>%s</td>' % data['summary'].encode('utf-8'))
                f_out.write('</tr>')
            # 写HTML结尾
            f_out.write('''
                </table>
                </body>
                </html>
            ''')
