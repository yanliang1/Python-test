# 基于百度翻译的翻译程序

import requests
import sys
import json

# 判断参数是否合法，如果参数个数不对，直接退出
if len(sys.argv) != 2:
    print("Usage:{}<word>".format(sys.argv[0]))
    sys.exit(1)

word = sys.argv[1] # 需要翻译的单词

url = "https://fanyi.baidu.com/sug"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
data = {"kw":word}

# 发送post请求到百度翻译服务器
res = requests.post(url,data = data,headers = headers)

# 返回的是一个json字串，转换成字典
res_dict = json.loads(res.content.decode())
# print(res_dict["data"])
# print(len(res_dict["data"]))

if res_dict["data"] == 0:
    print("翻译失败，请重新输入！")

# 解析，提取数据，显示到屏幕上
for item in res_dict["data"]:
    for v in item.values():
        print(v)
