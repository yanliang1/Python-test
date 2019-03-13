import requests
import bs4

res = requests.get("http://www.baidu.com")

html = res.content.decode()
print(type(html))
# with open("index.txt","w",encoding="utf-8") as f:
#     f.write(html)

soup = bs4.BeautifulSoup(html,"lxml")
print(type(soup))

# print(soup.prettify())
# print(soup.title.name)
# print(soup.link)
# print(soup.link.attrs["href"])
# print(soup.img.attrs.get("src"))

# select()用于寻找元素
# print(soup.select("span")) # 匹配所有的div标签
# print(soup.select("#su")) # 匹配ID是#su的标签
# print(soup.select(".lb")) # 匹配class为.lb的标签
# print(soup.select("div span")) # 匹配 div 下面的 span 标签
# print(soup.select("a[name]")) # 匹配 a 标签中 name 属性的标签
# print(soup.select("a[name = 'tj_login']")) # 匹配 a 标签中 name 属性值为 'tj_login' 的标签
# print(soup.select("a[name = 'tj_login']")[0].get_text()) # 获取文本内容 
# print(soup.select("p #link"))