import os
import requests
class Tieba_Spider:
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.header ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}


    def get_urls(self):
        urls = []    
        url = "https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}"
        for i in range(10):
            urls.append(url.format(self.tieba_name,i*50))
        return urls
        


    def get_response(self,url):
        res = requests.get(url,headers =self.header)
        return res.content.decode()


    def save_html(self,html,page_num):
        ok = os.path.exists(self.tieba_name)
        if not ok:
            os.makedirs(self.tieba_name)
        file_path = "{}/{}.html".format(self.tieba_name,page_num)
        f = open(file_path,"w",encoding="utf-8")
        f.write(html)
        f.close()


    def run(self):
        #1.获取URL列表
        urls =self.get_urls()
        print(urls)
        #2.遍历列表，获取响应
        for url in urls:
            ret = self.get_response(url)
            #3.保存响应结果
            page_num = urls.index(url) + 1
            self.save_html(ret,page_num)

if __name__ == "__main__" :
    tieba = Tieba_Spider("LOL")
    tieba.run()
