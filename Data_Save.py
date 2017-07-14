#coding = utf-8
import codecs
# import logging

class DataOutput(object):
    '''
    数据保存进html页面，单一每个数据是一个字典，数据量大的时候，这种方式非常的不科学
    '''
    # count = 0
    def __init__(self):
        self.datas = []
    def store_data(self, data):

        # logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        if data is None:
            return
        self.datas.append(data)
        # global count
        # count = count + 1
        # logging.info("正在进行保存")
    def output_html(self):

        with open('reviews.txt','w') as f:
            for data in self.datas:
                data = str(data)
                f.write(data)
        fout = codecs.open('Mtime_reviews', 'w', encoding = 'utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['影片名字'])
            fout.write("<td>%s</td>"%data['影评标题'])
            fout.write("<td>%s</td>" % data['影评网址'])
            fout.write("<td>%s</td>" % data['影评内容'])
            fout.write("<tr>")
            self.datas.remove(data)
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close