# -*- coding:UTF-8 -*-
import string
import urllib
from bs4 import BeautifulSoup
import requests


def get_html(server):
    try:
        response = requests.get(server)
        response.encoding = 'UTF-8'  # 改变编码
        print(response.encoding)
        html = response.text
        return html
    except:
        print('请求网址出错')


def cn_utf(name):
    url1 = 'http://122.200.75.13/' + name + '.html'
    post_url = urllib.parse.quote(url1, safe=string.printable)
    print(post_url)


server = 'http://122.200.75.13/'
target: str = 'http://122.200.75.13/%e6%98%93%e8%97%8f/%e6%9c%af%e6%95%b0/'
req = requests.get(url=target)
html = get_html(target)
div_bf = BeautifulSoup(html)
div = div_bf.find_all('div', class_='catalog')
a_bf = BeautifulSoup(str(div[0]))
a = a_bf.find_all("a")

for each in a:
    print(each.string)
    c = each.string
    b = each.string, server + each.get('href')
    cn_utf('易藏/术数/' + c)