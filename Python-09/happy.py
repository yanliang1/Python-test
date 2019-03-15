#coding:utf-8
import requests
from lxml import etree

url = "http://www.budejie.com/text/"

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

for i in range(1,51):   # 共有50页
    new_url = url + str(i)
    r = requests.get(new_url,headers = headers)
    # print(r.text)
    html = etree.HTML(r.content.decode())
    # ss = etree.parse(r)
    # duanziList = html.xpath('//div')
    # 找到a标签
    duanziList = html.xpath('//div[@class="j-r-list-c-desc"]/a')
    print(type(duanziList))
    print(duanziList)
    for duanzi in duanziList:
        print(duanzi.text)
        myFile = open("duanzi.txt", 'a') #追加形式打开文件
        myFile.write(duanzi.text)
        myFile.write('\n\n')
    print(i)
myFile.close()
print('全部完成')