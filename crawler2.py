# -*- coding: utf-8 -*-
"""
ZhangYu Editor

crawler2：requests库测试
"""

# 爬虫——通用代码框架
#import requests
#
#def getHTML(url):
#    try:
#        r = requests.get(url, timeout=30)   # 超时时间
#        r.raise_for_status()    # status不是200，抛出异常
#        r.encoding = r.apparent_encoding    # 保证解码正确
#        return r.text
#    except:
#        return "有异常"
#
## 入口
#if __name__ == "__main__":
#    url = "http://www.baidu.com"
#    print(getHTML(url))



# 图片爬取
#import requests
#import os
#url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
#root = "D://pics//"
#path = root + url.split('/')[-1]
#try:
#    if not os.path.exists(root):    # 路径不存在
#        os.mkdir(root)
#    if not os.path.exists(path):    # 文件不存在
#        r = requests.get(url)
#        if r.status_code == 200:
#            # 写入本地
#            with open(path, 'wb') as f:
#                f.write(r.content)
#            f.close()
#except:
#    print("爬取失败")



# 自动百度
#import requests
#url="http://www.baidu.com/s"
#r = requests.get(url, params={'wd':'Python'})
#print(r.status_code)
#print(r.request.url)
#print(len(r.text))



# 自动查询IP归属
#import requests
#url = 'http://m.ip138.com/ip.asp?ip='
#try:
#    r = requests.get(url + '202.204.80.112')
#    r.raise_for_status()
#    r.encoding = r.apparent_encoding
#    print(r.text[-500:])
#except:
#    print("爬取失败")



# beautifulsoup美化
import requests
url = "https://python123.io/ws/demo.html"
r = requests.get(url)
htmls = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(htmls, 'html.parser')
print(soup.prettify())



