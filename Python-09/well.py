from lxml import etree  # 解析模块
import requests  # 请求模块
import time  # 时间模块

# 写文件，用csv格式
with open('top250.csv','w',encoding='utf-8') as f:
    # top250书籍信息一共有10页，所以range为10
    for a in range(10):
        # 循环遍历url
        url = 'https://book.douban.com/top250?start={}'.format(a*25)

        # 伪装浏览器头部信息
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

        # 获取目标的url
        data = requests.get(url).text

        # 解析下载的数据
        s=etree.HTML(data)
        # 获取元素的Xpath信息 
        file=s.xpath('//*[@id="content"]/div/div[1]/div/table')
        print(type(file))
        print(file)
        # 延迟 防止被检测
        time.sleep(3)

        # 分别获取每个书籍的title、href、score、num、scrible信息
        for div in file:
            title = div.xpath("./tr/td[2]/div[1]/a/@title")[0]
            print(type(title))
            href = div.xpath("./tr/td[2]/div[1]/a/@href")[0]
            score = div.xpath("./tr/td[2]/div[2]/span[2]/text()")[0]
            num = div.xpath("./tr/td[2]/div[2]/span[3]/text()")[0].strip("(").strip().strip(")").strip()
            scrible = div.xpath("./tr/td[2]/p[2]/span/text()")

            # 判断，因为有的书籍没有描述信息，所以写入文件的时候需判断
            if len(scrible) > 0:
                f.write("{},{},{},{},{}\n".format(title,href,score,num,scrible[0]))
                print("书名：{}, 目标网址：{}, 评分：{}, 人数：{}, 评语：{}\n".format(title,href,score,num,scrible[0]))
            else:
                f.write("{},{},{},{}\n".format(title,href,score,num)) 
                print("{},{},{},{}\n".format(title,href,score,num))
        print("文件写入成功！")
    print(a)