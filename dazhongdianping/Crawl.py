import os
import csv
import requests
from bs4 import BeautifulSoup


def readHtml(path):
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(path)  # 返回该目录下的所有文件
    # 先添加目录级别
    index = 0;
    for f in files:
        try:
            file = open(path + '\\' + f, encoding='utf-8')  # 打开文件
            getData(file.read())  # file.read() 返回文件内容
            print(index)
            index+=1
        except Exception as e:
            print(e.reason)


def getData(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        compney_div = soup.find('div', class_='breadcrumb')
        len_c = len(compney_div.find_all('a'))
        compney = compney_div.find_all('a')[len_c - 1].text
        div = soup.find('div', class_='expand-info address')
        qu = div.find_all('span')[1].text
        add = div.find_all('span')[2].text
        a = soup.find('p', class_='expand-info tel')
        tel = a.find('span', class_='item').text

        bu_time = soup.find('div', 'other J-other Hide')
        bu_time = bu_time.find('span', class_='item').text.replace('\n', '').replace('                    ', '')

        compney = compney.replace('    ', '').replace('\n', '')
        address = qu + add.replace('\n', '').replace('        ', '')
        data = []
        data.append(compney)
        data.append(address)
        data.append(tel)
        data.append(bu_time)
        data.append('大众点评')
        writeCsv(data)
    except Exception as e:
        print(e)

def writeCsv(data):
    print(data)
    flag = os.path.exists('E:\meituan.csv')  # 文件是否存在
    with open('E:\meituan.csv', 'a', newline='') as csv_file:  # a是追加
        if flag:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data)
        else:  # 一开始不存在则写入表头
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['店铺名字', '公司地址', '联系方式', '营业时间', '数据来源'])
            csv_writer.writerow(data)


if __name__ == '__main__':
    readHtml('E:\html1')
