page_list = []
for i in range(50):
    if i == 0:
        # print(f"http://www.bjcjl.net/xyxw/index.html")
        page_list.append(f"http://www.bjcjl.net/xyxw/index.html")
    else:
        # print(f"http://www.bjcjl.net/xyxw/index{i}.html")
        page_list.append(f"http://www.bjcjl.net/xyxw/index_{i}.html")

import requests
from bs4 import BeautifulSoup

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
