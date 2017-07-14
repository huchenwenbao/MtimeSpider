#coding:utf-8

from time import sleep
from Get_Review_Urls import GetReviewsUrls
from Html_Downloader import HtmlDownloader
from Html_Parser import HtmlParser
from Data_Save import DataOutput


class Spider(object):
    def __init__(self):
        '''
        初始化，把自己写的模块引入进来
        '''
        self.download_urls = GetReviewsUrls()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.save = DataOutput()

    def crawl(self, root_url):
        '''
        主程序
        :param root_url:某个影片某个comment页面的url
        :return: 返回这个影片的各条影评
        '''


        if root_url is None:
            return
        html = self.downloader.download(root_url)
        review_urls = self.download_urls.get_urls(html)
        for each in review_urls:
            html_review = self.downloader.download(each)
            data = self.parser.parser(html_review)
            self.save.store_data(data)


if __name__=="__main__":
    import logging
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    Mtime_spider = Spider()
    global count
    count = 0
    # 设置下想爬取影评的数量
    while count < 100:
        # 时光网的影片的编号貌似是从10000~3000000不等，有些数字有影片有的没有，搞不懂
        # 如果是数字是空的还去访问，可能会浪费时间？
        for i in range(234000,235000):
            #第一个comment页面单独出来，因为没有‘-’
            Mtime_spider.crawl('http://movie.mtime.com/'+ str(i) +'/comment.html')
            #一个comment页面最多可以提取二十条影评信息，设置最多提取每个影片的200条长影评
            for j in range(2,10):
                Mtime_spider.crawl('http://movie.mtime.com/234923/comment-' + str(j) +'.html')
                count += 1
                logging.info("正在进行第%s条影评的爬取" % count)
            sleep(1)
    Mtime_spider.save.output_html()