# -*- coding: utf-8 -*-
"""
ZhangYu Editor

crawler4：淘宝商品
"""

import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def parsePage(glt, htmls):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', htmls)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', htmls)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            glt.append([price, title])
    except:
        print('no page')

def printGoodsList(glt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for good in glt:
        count += 1
        print(tplt.format(count, good[0], good[1]))

def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    goodsList = []
    for i in range(depth):  # 包括0、1，不包括2
        try:
            url = start_url + '&s=' + str(44*i)
            htmls = getHTMLText(url)
            parsePage(goodsList, htmls)
        except:
            continue
    printGoodsList(goodsList)
main()





















