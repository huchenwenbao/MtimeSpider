#coding=utf-8

import requests



class HtmlDownloader(object):

    def download(self, url):
        '''
        下载页面
        :param url: url
        :return: html
        '''
        if url is None:
            return
        user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers = headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text

        return None


if __name__=="__main__":
    a=HtmlDownloader()
    a = a.download('https://movie.douban.com/review/best/?start=0')

    print(a)
