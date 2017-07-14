# coding=utf-8

from bs4 import BeautifulSoup
from Html_Downloader import HtmlDownloader

class HtmlParser(object):

    def parser(self, html):
        '''
        提取所要的影评信息
        :param html:解析出的单一影评url由downloader传回来的html
        :return: 影评的具体信息们
        '''
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        data = {}

        soup = BeautifulSoup(html, 'lxml')

        #找出影片的名字
        a = soup.find('p',class_='mt15')
        data['影片名字'] = a.a.string

        #找出影评的标题
        review_title = soup.find(class_="px38 mt30 c_000")
        data['影评标题'] = review_title.string

        #影评的内容
        content = soup.find_all('div',class_="db_mediacont db_commentcont")  # 此时的content的属性为<class 'bs4.element.ResultSet'>
        for tag in content:
            data['影评内容'] = tag.text.strip()

        #影评的网址
        film_title = soup.find('p', class_="px14 lh18")
        data['影评网址'] = film_title.a['href']

        return data


if __name__=="__main__":
    a = HtmlParser()
    a.download = HtmlDownloader()
    html = a.download.download('http://movie.mtime.com/234923/reviews/8011185.html')
    print(a.parser(html))


