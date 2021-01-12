import numpy as np
from bs4 import BeautifulSoup
import requests


def get_html(url) -> object:
    try:
        response = requests.get(url)
        response.encoding = 'UTF-8'  # 改变编码
        print(response.encoding)
        html = response.text
        return html
    except:
        print('请求网址出错')


url = "http://122.200.75.13/%e6%98%93%e8%97%8f/%e6%9c%af%e6%95%b0/"
html = get_html(url)
bf = BeautifulSoup(html)
texts = bf.find_all('div', class_='row')
j = texts[0].text.replace('\xa0' * 8, '\n\n')
print(texts[0].text.replace('\xa0' * 8, '\n\n'))
file = open('explore.txt', 'a', encoding='utf-8')
file.write(j)
file.close()