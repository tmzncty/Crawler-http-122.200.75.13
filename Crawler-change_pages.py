import string
import urllib
from bs4 import BeautifulSoup
import requests


def get_html(post_url):  # 转码
    try:
        response = requests.get(post_url)
        response.encoding = 'UTF-8'  # 改变编码
        print(response.encoding)
        htm = response.text
        return htm
    except:
        print('请求网址出错')


def cn_utf(name):
    series = [i for i in range(1, 14, 1)]  # 生成1-13
    print(series)
    for z in series:
        print(z)
        if 1 == z:
            url1 = 'http://122.200.75.13/' + name + '.html'
            print(url1)
        else:
            url1 = 'http://122.200.75.13/' + name + "-" + f"{z}" + '.html'
            print(url1)
        post_url = urllib.parse.quote(url1, safe=string.printable)
        print(post_url)
        r = requests.get(post_url)
        print(r.status_code)
        if 200 == r.status_code:
            print('有效')

            # 转码+输出
            htm = get_html(post_url)
            bf = BeautifulSoup(htm)
            texts = bf.find_all('div', class_='row')
            j = texts[0].text.replace('\xa0' * 8, '\n\n')
            print(texts[0].text.replace('\xa0' * 8, '\n\n'))
            file = open('12.txt', 'a', encoding='utf-8')
            file.write(j)
            file.close()
        else:
            print('无效')
        print(r)


# 遍历目录
server = 'http://122.200.75.13/'
target: str = "http://122.200.75.13/%e6%98%93%e8%97%8f/%e6%9c%af%e6%95%b0/"
req = requests.get(url=target)
html = get_html(target)
div_bf = BeautifulSoup(html)
div = div_bf.find_all('div', class_='catalog')
a_bf = BeautifulSoup(str(div[0]))
a = a_bf.find_all("a")

for each in a:
    c = each.string
    b = each.string, server + each.get('href')
    cn_utf('易藏/术数/' + c)  # 执行上面的函数
    print(b)
