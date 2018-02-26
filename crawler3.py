# -*- coding: utf-8 -*-
"""
ZhangYu Editor

crawler3：中国大学排名
"""

import requests
from bs4 import BeautifulSoup
from bs4 import element

def getHTMLText(url):
    '''
        根据url获取htmls
    '''
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text        
    except:
        return ''

def fillUinfoList(uinfo, htmls):
    '''
        从htmls中提取大学信息，放入uinfo
    '''
    soup = BeautifulSoup(htmls, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, element.Tag):
            tds = tr('td')
            uinfo.append([tds[0].string, tds[1].string, tds[3].string])

def printUinfoList(uinfo, num):
    '''
        输出uinfo的前num行
    '''
    tplt1 = "{0:^10}\t{1:{3}^8}\t{2:^9}"
    tplt2 = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt1.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u = uinfo[i]
        print(tplt2.format(u[0],u[1],u[2],chr(12288)))
    
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    htmls = getHTMLText(url)
    fillUinfoList(uinfo, htmls)
    printUinfoList(uinfo, 20)

main()