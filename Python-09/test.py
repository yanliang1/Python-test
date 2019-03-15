import requests
import os
from lxml import etree

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

def get_text(url):
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    dom = etree.HTML(r.text)
    return dom


def get_imgage(url, name, px):
    r = requests.get(url, headers=headers)
    if (r.status_code != 200):
        print("图片下载失败")
        return
    r.encoding = r.apparent_encoding
    f = open(f'{name}-{px}.jpg', 'wb')
    f.write(r.content)


def create_file():
    path = os.getcwd() + "\image"
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)


def get_name_href(dom):
    name = dom.xpath('//li[@class="photo-list-padding"]//em//text()')
    href = dom.xpath('//li[@class="photo-list-padding"]//@href')
    return name, href


def getImgHref_Px(href):
    dom = get_text(href)
    try:
        px = dom.xpath('//dd[@id="tagfbl"]//a//@id')[0]
        imgage_url = dom.xpath('//dd[@id="tagfbl"]//a[@target="_blank"]//@href')[0]
        dom_1 = get_text(host + imgage_url)
        imgage_href = dom_1.xpath('//img//@src')[0]
        return imgage_href, px
    except:
        imgage_href = dom.xpath('//div[@id="mouscroll"]//img//@src')[0]
        return imgage_href, "960x600"


host = "http://desk.zol.com.cn"
target = "http://desk.zol.com.cn/dongman/"
cnt = 0
create_file() 

for x in range(1, 42):
    dom = get_text("http://desk.zol.com.cn/dongman/" + str(x) + ".html")
    name, href = get_name_href(dom)
    for i in range(0, len(href)):
        cnt = cnt + 1
        print("正在下载" + str(cnt) + ":" + name[i])
        imgHref, px = getImgHref_Px(host + href[i])
        get_imgage(imgHref, name[i], px)