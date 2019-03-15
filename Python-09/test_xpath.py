
from lxml import etree
import requests

url = "https://www.qidian.com/finish?chanId=22&action=hidden&orderId=&page=1&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=2"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

res = requests.get(url,headers=headers)

html = etree.HTML(res.content.decode())

#text = html.xpath("/html/body/div[2]/div[5]/div[2]/div[2]/div/ul/li[1]/div[2]/p[2]/text()")
# text = html.xpath("//ul[@class='all-img-list cf']//li//p[@class='intro']/text()")
#text = html.xpath("//ul[@class='all-img-list cf']//li//a/@href")
text = html.xpath("//ul[@class='all-img-list cf']//li//img/@src")

print(type(text))
print(text[0].strip())

#保存图片
img_src = "https:" + text[0].strip()
res = requests.get(img_src)
with open("ddzf.png","wb") as f:
	f.write(res.content)



