#!/usr/bin/python3
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

emule = []
baidu = []

tv_url = input('请输入剧集地址\n格式为: http://www.zimuxia.cn/portfolio/[剧集名]\n')

with requests.Session() as session:
    resp = session.get(tv_url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.content, 'lxml', from_encoding=resp.encoding)

    emule_text = soup.find_all(text='电驴下载')
    for i in range(len(emule_text)):
        emule_parent = emule_text[i].parent
        emule.append(emule_parent.get('href'))

    baidu_text = soup.find_all(text='百度网盘')
    for j in range(len(baidu_text)):
        baidu_parent = baidu_text[j].parent
        baidu.append(baidu_parent.get('href'))

print('ed2k:')
for m in range(len(emule)):
    print(emule[m])

print('百度云:')
for n in range(len(baidu)):
    print(baidu[n])
