#!/usr/bin/python
# -*- coding:utf8 -*-

import os
import csv
from bs4 import BeautifulSoup

def readHtml(path):
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(path)    #返回该目录下的所有文件
    # 先添加目录级别
    for f in files:
        file = open(path + '\\' + f)    #打开文件
        getDataToExcel(file.read())     #file.read() 返回文件内容



def getDataToExcel(html):
    soup = BeautifulSoup(html, 'html.parser')
    li_arr = soup.find_all('li', class_='company-list-item')

    for li in li_arr:
        company = li.find('a', class_='list-item-title-text')           #获取class值为:list-item-title-text 的a标签
        address = li.find('a', class_='sm-offerResult-areaaddress')     #获取class值为:sm-offerResult-areaaddress 的a标签
        data = [company.get('title'), company.get('href'), address.get('title')]    #获取a标签中的值使用get('title')
        print(data)
        writeCsv(data)

'''写入数据到csv中'''
def writeCsv(data):
    flag = os.path.exists('E:\write.csv')   #文件是否存在
    with open('E:\write.csv', 'a', newline='') as csv_file:     #a是追加
        if flag :
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data)
        else:   #一开始不存在则写入表头
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['公司名称', '淘宝地址', '公司办公地址', ])


if __name__ == '__main__':
    readHtml('E:\html')