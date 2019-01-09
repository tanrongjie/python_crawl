import os
import csv
import requests
import time
import random
import datetime
from bs4 import BeautifulSoup


def crawlUrl(url, refere):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache - Control': 'no - cache',
        'Connection': 'keep-alive',
        'cookie': '_lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=16825eadaddc8-0119b171438e07-b79183d-1fa400-16825eadadec8; _lxsdk=16825eadaddc8-0119b171438e07-b79183d-1fa400-16825eadadec8; _hc.v=7a262767-9861-9806-0362-a68c84966d5f.1546824375; cy=7; cye=shenzhen; s_ViewType=10; _lxsdk_s=1682b7f0094-43f-888-384%7C%7C83',
        'Host': 'www.dianping.com',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'Referer': refere,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    # f = open('a.html', 'rb')
    res = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    print(res.text)
    # arr = soup.find_all({'data-click-name':'shop_title_click'})
    arr = soup.find_all('a')
    for a in arr:
        if a.get('data-click-name') == 'shop_title_click':
            getHtml(a.get('href'), url)
            time.sleep(1)
            print('写入完一次文件:')
            time1_str = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            print(time1_str)


def getHtml(url, refere):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache - Control': 'no - cache',
        'Connection': 'keep-alive',
        'cookie': 'cy=7; cityid=7; cye=shenzhen; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=16825eadaddc8-0119b171438e07-b79183d-1fa400-16825eadadec8; _lxsdk=16825eadaddc8-0119b171438e07-b79183d-1fa400-16825eadadec8; _hc.v=7a262767-9861-9806-0362-a68c84966d5f.1546824375; cy=7; cye=shenzhen; s_ViewType=10; _lxsdk_s=1682b7f0094-43f-888-384%7C%7C107',
        'Host': 'www.dianping.com',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'Referer': refere,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    time.sleep(random.randint(10, 25))
    res = requests.get(url=url, headers=headers)
    time1_str = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    print('写入中:')
    print(time1_str)
    try:
        html = res.text
        t = time.time()
        filename = 'E:\\html1\\html_' + str(int(t)) + '.txt'
        print(filename)
        with open(filename, 'w', encoding='utf-8') as fileobject:  # 使用‘w’来提醒python用写入的方式打开
            fileobject.write(html)
    except Exception as e:
        print(e.reason)
    time.sleep(6)


if __name__ == '__main__':
    for i in range(15, 50):
        url = 'http://www.dianping.com/search/keyword/7/0_%E7%BE%8E%E5%AE%B9%E4%BC%9A%E6%89%80/p' + str(i)
        refere = 'http://www.dianping.com/search/keyword/7/0_%E7%BE%8E%E5%AE%B9%E4%BC%9A%E6%89%80/p' + str(i - 1)
        crawlUrl(url, refere)
        if i % 5 == 0:
            time.sleep(random.randint(15, 35))
