#!/usr/bin/python3
# -*- coding:utf-8 -*-

# Thanks: CodesW(https://www.cnblogs.com/tp1226/p/8419564.html)

import requests
from bs4 import BeautifulSoup

domain = 'http://www.zhuixinfan.com/'
emule = []
baidu = []
weiyun = []

tv_url = input('请输入剧集地址\n格式为: http://www.zhuixinfan.com/viewtvplay-[数字].html\n')

with requests.Session() as session:
    resp = session.get(tv_url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.content, 'lxml', from_encoding=resp.encoding)
    tag_resources = soup.find(id='ajax_tbody')
    for res in tag_resources.find_all('tr'):
        tag_a = res.find('a')

        res_url = domain + tag_a.get('href')
        resp = session.get(res_url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.content, 'lxml', from_encoding=resp.encoding)

        emule_url = soup.find(id='emule_url')
        emule.append(emule_url.get_text())

        baidu_text = soup.find(text='网盘下载1')
        if baidu_text != None:
            baidu_parent = baidu_text.parent
            baidu.append(baidu_parent.get('href'))

        weiyun_text = soup.find(text='网盘下载2')
        if weiyun_text != None:
            weiyun_parent = weiyun_text.parent
            weiyun.append(weiyun_parent.get('href'))

print('ed2k:')
for i in range(len(emule)):
    print(emule[i])

if baidu == []:
    print('无百度云链接')
else:
    print('百度云:')
    for j in range(len(baidu)):
        print(baidu[j])

if weiyun == []:
    print('无微云链接')
else:
    print('微云:')
    for k in range(len(weiyun)):
        print(weiyun[k])

input('Press ENTER to exit …')
