
import requests
from bs4 import BeautifulSoup

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
            link_list.append(href['href'])
        # %s, %d, %f
        print("爬了[%s]%d个链接" % ( url , len(hrefs)) )
    print(link_list)
    return link_list

# all_link_list = get_list()

"""
css selector
".detail .detail_tit h3"
"""
page_link = "http://www.bjcjl.net/xyxw/202207/t20220719_80096.html"
strhtml = requests.get(page_link)
strhtml.encoding = 'utf-8'
html_doc = strhtml.text
# 创建一个BeautifulSoup解析对象
soup = BeautifulSoup(html_doc, "html.parser")
# 获取所有的链接
title = soup.select(".detail .detail_tit h3")
contents = soup.select(".nr .TRS_Editor div")
print(type(contents))

# 我要收集所有的内容
content_list = []

for content in contents:
    content_list.append(content.text)
    #print(content.text)

# print(content_list)
# print("-"*80)
# file = open("test.txt","w")
# for c in content_list:
#     file.write(c.strip())
# file.close()
file = open("chenjinglun.txt","w")
file.write(str(title))
for text in content_list:
    # print(text)
    file.write(text)
file.close()
