import string
import urllib

import requests


def hh(name):
    series = [i for i in range(1, 14, 1)]  # 生成1-13
    print(series)
    for z in series:
        print(z)
        if z == 1:
            url = 'http://122.200.75.13/' + name + '.html'
            print(url)
        else:
            url = 'http://122.200.75.13/' + name + "-" + f"{z}" + '.html'
            print(url)
        post_url = urllib.parse.quote(url, safe=string.printable)
        print(post_url)
        r = requests.get(post_url)
        print(r.status_code)
        if 200 == r.status_code:
            print('有效')
        else:
            print('无效')
        print(r)
    exit()

hh('易藏/术数/葬书')
