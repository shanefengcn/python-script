#!/usr/bin/python3
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

baidu = []
qingt = []
magnet = []
emule = []

tv_url = input('请输入剧集地址\n格式为: http://www.zimuxia.cn/portfolio/[剧集名]\n')

with requests.Session() as session:
    resp = session.get(tv_url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.content, 'lxml', from_encoding=resp.encoding)

    baidu_text = soup.find_all(text='百度网盘')
    if baidu_text != None:
        for i in range(len(baidu_text)):
            baidu_parent = baidu_text[i].parent
            baidu.append(baidu_parent.get('href'))

    qingt_text = soup.find_all(text='青铜网盘')
    if qingt_text != None:
        for i in range(len(qingt_text)):
            qingt_parent = qingt_text[i].parent
            qingt.append(qingt_parent.get('href'))
    
    magnet_text = soup.find_all(text='磁力下载')
    if magnet_text != None:
        for j in range(len(magnet_text)):
            magnet_parent = magnet_text[j].parent
            magnet.append(magnet_parent.get('href'))

    emule_text = soup.find_all(text='电驴下载')
    if emule_text != None:
        for k in range(len(emule_text)):
            emule_parent = emule_text[k].parent
            emule.append(emule_parent.get('href'))

if baidu == []:
    print('无百度云链接')
else:
    print('百度云:')
    for i in range(len(baidu)):
        print(baidu[i])

if qingt == []:
    print('无青铜链接')
else:
    print('青铜:')
    for i in range(len(qingt)):
        print(qingt[i])

if magnet == []:
    print('无磁力链')
else:
    print('磁力链:')
    for j in range(len(magnet)):
        print(magnet[j])

if emule == []:
    print('无ed2k链接')
else:
    print('ed2k:')
    for k in range(len(emule)):
        print(emule[k])

input('Press ENTER to exit …')
