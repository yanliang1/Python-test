import requests
import sys
import json

url = "https://fanyi.baidu.com/sug"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

idata = input("请您输入需要查询的内容：")

data = {
    "kw":idata
}

#发送post请求
res = requests.post(url,data = data,headers = headers)
# print(res.status_code)
# print(res.content)
# print(type(res.content))

d = json.loads(res.content.decode())
# print(type(d))
# print(d['data'])

da = d['data']
# print(type(da))
print("您查询的内容的翻译结果为：",da[0]['v'])
# print(type(da[0]))
# print(res.content.decode())

f = open("f.html","w",encoding="utf-8")
f.write(res.content.decode())
f.close()