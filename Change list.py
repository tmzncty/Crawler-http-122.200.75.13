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


server = 'http://122.200.75.13/'
target: str = "http://122.200.75.13/%e5%84%92%e8%97%8f/"
req = requests.get(url=target)
html = get_html(target)
div_bf = BeautifulSoup(html)
div = div_bf.find_all('div', class_='catalog')
a_bf = BeautifulSoup(str(div[0]))
a = a_bf.find_all("a")
print(a)
str1 = str(a)
print(str1)
print(type(a))
print(isinstance(a, list))
print(isinstance(str1, list))
print(str1.split('/')[0])
print(str1.split('/')[1] + "/" + str1.split('/')[2])
str2 = str1.split('/')[1] + "/" + str1.split('/')[2]
print(str2)
print(str2.split('/')[0] + "/" + str2.split('/')[1])
for each in a:
    b = server + each.get('href')
    print(b)
    r = requests.get(b)
    print(r.status_code)
    server = 'http://122.200.75.13/'
    target: str = b
    req = requests.get(url=target)
    html = get_html(target)
    div_bf = BeautifulSoup(html)
    div = div_bf.find_all('div', class_='catalog')
    a_bf = BeautifulSoup(str(div[0]))
    a = a_bf.find_all("a")
    print(a)
    for eac in a:
        b = server + eac.get('href')
        print(b)
        r = requests.get(b)
        print(r.status_code)
