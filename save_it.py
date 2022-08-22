import os

import requests
from bs4 import BeautifulSoup


def save_one_page(page_link):
    # 如果下载目录不存在，就创建它
    if not os.path.exists("./data"):
        os.mkdir("./data")

    # 爬取一个页面数据
    # page_link = "http://www.bjcjl.net/xyxw/202207/t20220719_80096.html"
    file_name = page_link.split("/")[-1].replace('html', 'txt')

    if os.path.exists(os.path.join("./data", file_name)):
        return "file_name存在!!"

    # 创建一个BeautifulSoup解析对象
    strhtml = requests.get(page_link)
    strhtml.encoding = 'utf-8'
    html_doc = strhtml.text
    soup = BeautifulSoup(html_doc, "html.parser")

    # 保存图片文件
    images = soup.select(".nr .TRS_Editor img")
    number = 1
    for image in images:
        #  "xxxx.txt" => "xxxx.jpg"
        #  "xxxx.txt" => "xxxx_i.jpg"
        # "https://www.abc.com/aaa/bb/cc.html"
        image_url = page_link[:page_link.rfind("/")] + image.get('src')[1:]
        print("下载图片：", image_url)
        img_data = requests.get(image_url).content
        image_name = file_name.replace('.txt', '_' + str(number) + '.jpg')
        image_file = open(os.path.join("./data", image_name), "wb")
        image_file.write(img_data)
        number = number + 1

    # 获取所有的链接
    title = soup.select(".detail .detail_tit h3")[0].text
    contents = soup.select(".nr .TRS_Editor")
    # 我要收集所有的内容
    content_list = []
    for content in contents:
        content_list.append(content.text)
    # 保存文本文件
    file = open(os.path.join("./data", file_name), "w")
    file.write(str(title))
    for text in content_list:
        # print(text)
        file.write(text)
    file.close()


    return file_name