import os
import csv
import requests
import time
import random
from bs4 import BeautifulSoup


def openMerchantInfo(url, index):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache - Control': 'no - cache',
        'Connection': 'keep-alive',
        'cookie': '__mta=150435465.1546662362307.1547010384573.1547010395470.3; _lxsdk_cuid=1681c42bc64c8-0fb5d705bd3714-b79183d-1fa400-1681c42bc6653; __mta=150435465.1546662362307.1546662362307.1546662362307.1; ci=30; rvct=30%2C91%2C1; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; mtcdn=K; u=1558935050; n=RM_TRJ; lt=ex4otqz8mcdyGFKoqr6lnqJe9mUAAAAAvwcAAFaShismuFmvSJqEtauGxcMVCIw39Odrcob_qDO4IOTZ0qJTBGK8lywyIebESLZA4w; lsu=; token2=ex4otqz8mcdyGFKoqr6lnqJe9mUAAAAAvwcAAFaShismuFmvSJqEtauGxcMVCIw39Odrcob_qDO4IOTZ0qJTBGK8lywyIebESLZA4w; uuid=f3751401ac2746a28afc.1546701937.2.0.0; _lxsdk=1681c42bc64c8-0fb5d705bd3714-b79183d-1fa400-1681c42bc6653; unc=RM_TRJ; _lxsdk_s=16830f6ed61-9f9-720-806%7C%7C' + str(index),
        'Host': 'www.meituan.com',
        'Pragma': 'no-cache',
        'Referer': 'https://sz.meituan.com/s/%E7%BE%8E%E5%AE%B9%E9%9D%A2%E9%83%A8%E6%8A%A4%E7%90%86/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    time.sleep(random.randint(0, 5))
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    # 获取公司名称
    try:
         company = soup.find('h1', class_='seller-name').text
         items = soup.find_all('div', class_='item')
         # 获取地址和联系方式
         info = []
         info.append(company)
         for item in items:
             span = item.find_all('span')[1].text.replace('\n', '')
             if span.strip() == '':
                 span = '暂无'
             info.append(span)
         info.append('美团')
         writeCsv(info)
    except Exception as err:
        print(err)
    time.sleep(5)

'''写入数据到csv中'''


def writeCsv(data):
    print(data)
    flag = os.path.exists('meituan.csv')  # 文件是否存在
    with open('meituan.csv', 'a', newline='') as csv_file:  # a是追加
        if flag:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data)
        else:  # 一开始不存在则写入表头
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['店铺名字', '公司地址', '联系方式', '营业时间', '数据来源'])
            csv_writer.writerow(data)


if __name__ == '__main__':
    res = requests.get('http://127.0.0.1/Crawl/crawl.php')
    ids = res.text.split(',')

    index = 74
    for id in ids:
        url = 'https://www.meituan.com/jiankangliren/' + str(id) + '/'
        openMerchantInfo(url, index)
        time.sleep(10)
        index += 2
