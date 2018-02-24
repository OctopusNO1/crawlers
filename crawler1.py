'''
    熊猫TV的LOL主播的人气排名
'''

from urllib import request
import re

class Spider():
    '''
        爬虫类
    '''
    url = 'https://www.panda.tv/cate/lol'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    # 抓取源代码
    def __fetch_content(self):  # __ 私有方法private
        r =request.urlopen(Spider.url)
        htmls_bytes = r.read()
        htmls = str(htmls_bytes, encoding = 'utf-8')
        a = 1
        return htmls

    # 分析、抓取标签
    def __analysis(self, htmls):
        root_htmls = re.findall(Spider.root_pattern, htmls)
        anchors = []
        a = 0
        for root_html in root_htmls:
            name_html = re.findall(Spider.name_pattern, root_html)
            number_html = re.findall(Spider.number_pattern, root_html)
            anchor = {'name':name_html, 'number':number_html}
            anchors.append(anchor)
            a += 1
        a = 2
        return anchors

    # 数据精炼、清洗
    def __refine(self, anchors):
        l = lambda anchor:{
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
            }
        refined_anchors = list(map(l, anchors))
        return refined_anchors

    # 数据排序
    def __sort(self, anchors):
        sorted_anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return sorted_anchors
    
    # 按人数number排序
    def __sort_seed(self, anchor):
        r = re.findall('\d*', anchor['number']) # 提取数字
        number = float(r[0])                    # str转换成float
        if '万' in anchor['number']:            # 万 *10000
            number *= 10000
        return number

    # 格式化输出
    def __show(self, anchors):
        for i in range(0, len(anchors)):
            print('rank:' + str(i+1) + '   ' + anchors[i]['name'] + '------' + anchors[i]['number'])

    # 入口方法
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        refined_anchors = self.__refine(anchors)
        sorted_anchors = self.__sort(refined_anchors)
        self.__show(sorted_anchors)

spider = Spider()
spider.go()
