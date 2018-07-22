#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
import json

import requests


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


config = configparser.ConfigParser()
config.read('Update.ini')
mobile = config['Default']['mobile']
imei = config['Default']['imei']
version_a = config['Version']['version_a']
version_x = config['Version']['version_x']
version_w = config['Version']['version_w']

url = 'http://otag.h2os.com/post/Query_Update'
headers = {'User-Agent': 'com.oneplus.opbackup/1.4.0.171219144846.50044e6',
           'Content-Type': 'application/json'}
body_A = {'version': '1', 'mobile': mobile, 'ota_version': version_a, 'imei': imei,
          'mode': '0', 'type': '1', 'language': 'zh-CN', 'beta': '0', 'isOnePlus': '1'}
body_X = {'version': '1', 'mobile': mobile, 'ota_version': version_x, 'imei': imei,
          'mode': '0', 'type': '1', 'language': 'zh-CN', 'beta': '0', 'isOnePlus': '1'}
body_W = {'version': '1', 'mobile': mobile, 'ota_version': version_w, 'imei': imei,
          'mode': '0', 'type': '1', 'language': 'zh-CN', 'beta': '0', 'isOnePlus': '1'}
response_A = requests.post(url, json=body_A, headers=headers, timeout=60)
response_X = requests.post(url, json=body_X, headers=headers, timeout=60)
response_W = requests.post(url, json=body_W, headers=headers, timeout=60)

if response_A.status_code == 200:
    json_A = json.loads(response_A.text, object_hook=JSONObject)
    new_version_A = json_A.new_version
    extract_A = json_A.extract
    extract_A = extract_A.replace('\\\\\n', '')
    extract_A = extract_A.replace('\\\\n', '')
    extract_A = extract_A.replace('\\\n', '')
    extract_A = extract_A.replace('\\n', '')
    download_A = json_A.down_url
    print('new stable version:', new_version_A)
    print(extract_A)
    print(download_A)
    config['Version']['version_a'] = new_version_A
elif response_A.status_code == 304:
    print('no new stable version')
else:
    print('Update stable version: HTTP', response_A.status_code)

if response_X.status_code == 200:
    json_X = json.loads(response_X.text, object_hook=JSONObject)
    new_version_X = json_X.new_version
    extract_X = json_X.extract
    extract_X = extract_X.replace('\\\\\n', '')
    extract_X = extract_X.replace('\\\\n', '')
    extract_X = extract_X.replace('\\\n', '')
    extract_X = extract_X.replace('\\n', '')
    download_X = json_X.down_url
    print('new beta version:', new_version_X)
    print(extract_X)
    print(download_X)
    config['Version']['version_x'] = new_version_X
elif response_X.status_code == 304:
    print('no new beta version')
else:
    print('Update beta version: HTTP', response_X.status_code)

if response_W.status_code == 200:
    json_W = json.loads(response_W.text, object_hook=JSONObject)
    new_version_W = json_W.new_version
    extract_W = json_W.extract
    extract_W = extract_W.replace('\\\\\n', '')
    extract_W = extract_W.replace('\\\\n', '')
    extract_W = extract_W.replace('\\\n', '')
    extract_W = extract_W.replace('\\n', '')
    download_W = json_W.down_url
    print('new alpha version:', new_version_W)
    print(extract_W)
    print(download_W)
    config['Version']['version_w'] = new_version_W
elif response_W.status_code == 304:
    print('no new alpha version')
else:
    print('Update alpha version: HTTP', response_W.status_code)

config.write(open('Update.ini', 'r+'))

input('Press ENTER to exit …')
