#requests入门示例

import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}

#发起请求，得到响应
response = requests.get("https://www.baidu.com/",headers=headers) 
#查看响应类型
print(type(response))	
#查看响应的编码格式  ISO-8859-1 不能正常显示中文
print(response.encoding)
#查看响应的状态，200表示成功 
print(response.status_code)
#查看响应的文本(字符串)
#print(response.text)
#查看响应的原始数据(原始字节)
content = response.content
#查看响应内容的类型
print(type(content))
#解码响应内容，解码格式为utf-8
#print(content.decode("utf-8"))

f = open("baidu.html","wb")
f.write(content)
f.close()






# <img src="https://timgmb04.bdimg.com/timg?searchbox_feed&amp;quality=100&amp;size=w1024&amp;sec=0&amp;di=b300e94464efaf9537bf580832f4ae03&amp;src=http%3A%2F%2Ft10.baidu.com%2Fit%2Fu%3D4139872554%2C2860621297%26fm%3D175%26app%3D25%26f%3DJPG%3Fw%3D218%26h%3D146%26s%3D579471857826DED8081C68E60300C032">