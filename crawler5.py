# -*- coding: utf-8 -*-
"""
ZhangYu Editor

crawler5：股票名称、交易信息
"""

import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url, code='utf-8'):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text[:20000]
    except:
        return ''

def getStockList(lst, stockURL):
    # 股票概况页面，获取股票href，放入list
    htmls = getHTMLText(stockURL, 'GB2312')
    soup = BeautifulSoup(htmls, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])    # 如sh500010
        except:
            continue

def getStockInfo(lst, stockURL, fpath):
    # 遍历list，生成url-list，进入详细页面
    count = 0  
    for stock in lst:
        url = stockURL + stock + ".html"    # 生成该股票详细页面
        htmls = getHTMLText(url)
        try:
            infoDict = {}   # 清空股票信息
            if htmls == "":
                # infoDict.update({'股票名称':'empty'})
                print('empty')
            else:
                # 获取详细页面的股票信息
                soup = BeautifulSoup(htmls, 'html.parser')
                stockInfo = soup.find('div', attrs={'class':'stock-bets'})
                if stockInfo:   # 非空
                    # 获取股票名称
                    name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
                    infoDict.update({'股票名称':name.text.split()[0]})
                    # 获取股票信息
                    keyList = stockInfo.find_all('dt')
                    valueList = stockInfo.find_all('dd')
                    for i in range(len(keyList)):
                        key = keyList[i].text
                        val = valueList[i].text
                        infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count += 1
                print("当前进度:{:.2f}%,count={},len={}".format(count*100/len(lst), count, len(lst)), end="\n")  # 默认为\n
                # print("\r当前进度：{:.2f}%".format(count*100/len(lst)), end="")    # 动态显示，命令行
        except:
            # traceback.print_exc()   # 打印异常信息
            count += 1
            print("error-----当前进度:{:.2f}%".format(count*100/len(lst)), end="\n")  
            continue

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D://BaiduStockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)
    
main()
    
    