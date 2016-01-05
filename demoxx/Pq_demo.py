from pyquery import PyQuery as pq
from urllib.request import urlopen

class UrlParser():
    def __init__(self):
        self.urls = []
    def feed(self):
        d = pq(url='http://hao123.com')
        if d.find('a'):
            url = d('a').map(lambda i, e: pq(e)('a').attr('href'))
            for u in url:
                self.urls.append(u)
    def geturls(self):
        return self.urls

if __name__ == '__main__':
    urls = []
    url = UrlParser()
    url.feed()
    urls += url.geturls()
    print('被提取的所有url为:\n',urls)
    dlink = urls[-1]
    response = urlopen(dlink)
    print ('最后一个url的响应状态为:',response.status)
