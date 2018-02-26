# -*- coding: utf-8 -*-
"""
ZhangYu Editor

crawler6:爬取图片及名称
"""

import requests
from bs4 import BeautifulSoup
import os

def getHTML(url, code='utf-8'):
    response = requests.get(url, timeout=30)
    response.raise_for_status() 
    response.encoding = code 
    html = response.text
    return html

def getInfoPic(html):
    info_pic_dict = {}
    soup = BeautifulSoup(html, 'html.parser')
    for li in soup.find(id='contents').find_all('li'):
#        name = li.h5.a.string
        url = li.a.img.attrs['src']
        name = url.split('/')[-1]
        info_pic_dict[name] = url
    return info_pic_dict
    
def writeOut(info_pic_dict, root):
    if not os.path.exists(root):    
        os.mkdir(root)
    for name in info_pic_dict:
        path = root + name + '.jpg'
        if not os.path.exists(path):
            url = info_pic_dict[name]
            response = requests.get(url)
            with open(path, 'wb') as f:
                f.write(response.content)
            f.close()

url_root = 'http://aqdybg.com/guochan/index'
root = 'D:/pics/' 
pageCount = 3

#for i in range(pageCount):
#    if i == 0:
#        url = url_root + '.html'
#    else:
#        url = url_root + str(i+1) + '.html'
#    html = getHTML(url,'gbk')
#    info_pic_dict = getInfoPic(html)
#    writeOut(info_pic_dict, root)

url = url_root + '3.html'
html = getHTML(url,'gbk')
info_pic_dict = getInfoPic(html)
writeOut(info_pic_dict, root)
