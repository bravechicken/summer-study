import os
import time

import requests
from bs4 import BeautifulSoup

# from save_it import save_one_page
import  save_it

def get_list():
    page_list = []
    for i in range(50):
        if i == 0:
            # print(f"http://www.bjcjl.net/xyxw/index.html")
            page_list.append(f"http://www.bjcjl.net/xyxw/index.html")
        else:
            # print(f"http://www.bjcjl.net/xyxw/index{i}.html")
            page_list.append(f"http://www.bjcjl.net/xyxw/index_{i}.html")

    link_list = []
    for url in page_list:
        # url = "http://www.bjcjl.net/xyxw/index.html"
        strhtml = requests.get(url)
        strhtml.encoding = 'utf-8'
        html_doc = strhtml.text
        # 创建一个BeautifulSoup解析对象
        soup = BeautifulSoup(html_doc, "html.parser")
        # 获取所有的链接
        hrefs = soup.select(".detail_list li a")

        for href in hrefs:
            link_list.append("http://www.bjcjl.net/xyxw/" + href['href'][2:])
        # %s, %d, %f
        print("爬了[%s]%d个链接" % (url, len(hrefs)))
    print(link_list)
    return link_list


# all_link_list = get_list()

"""
css selector
".detail .detail_tit h3"
"""





if __name__ == '__main__':
    # 获得所有的链接列表
    list = get_list()

    # 循环每一个链接，去爬取链接对应的内容
    for i, link in enumerate(list):
        try:
            print("要爬 %s %d/%d" % (link, i + 1, len(list)))
            # 另存为文本文件和图片
            print(save_it.save_one_page(link))
        except Exception as e:
            print("爬取[%s]出现问题：%s" % (link, str(e)))
