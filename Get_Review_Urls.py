#coding=utf-8

from bs4 import BeautifulSoup
from Html_Downloader import HtmlDownloader
import re

class GetReviewsUrls(object):

    #获取影片首页的html
    def get_urls(self, html):
        '''
        获取各条影评的url
        :param html: 包含各条影评的comment页面的html
        :return: 影评们的urls
        '''

        res = []
        soup = BeautifulSoup(html, 'lxml', from_encoding='utf-8')
        reviews_urls = soup.find_all('a', class_= "px12 ml6")
        cell = [i for i in reviews_urls]  # 把网址从resultset中拿出来
        # print(len(cell))
        cell = map(lambda x: str(x), cell)  # 把cell列表里面的每一个tag元素都变成列表
        # 第一种：非常笨的用数数的方法数出网址
        # for j in cell:
        #     print(j[26:76])
        # 第二种：正则表达式
        pattern = re.compile(r'http://(.*?)html')
        for i in cell:
            result = re.search(pattern, i)
            res.append(result.group())
        return res


if __name__=="__main__":
    a = GetReviewsUrls()
    a.download = HtmlDownloader()
    html = a.download.download("http://movie.mtime.com/234923/comment.html")
    print(a.get_urls(html))

