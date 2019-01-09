#!/usr/bin/python
# -*- coding:utf8 -*-

import os
import csv
import requests
from bs4 import BeautifulSoup

def readHtml(path):
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(path)    #返回该目录下的所有文件
    # 先添加目录级别
    i = 0
    for f in files:
        if i > 1 and i <= 2:
            file = open(path + '\\' + f)    #打开文件
            getDataToExcel(file.read())     #file.read() 返回文件内容
        i += 1


"""
读取文本中存入的阿里巴巴列表数据
"""
def getDataToExcel(html):
    soup = BeautifulSoup(html, 'html.parser')
    li_arr = soup.find_all('li', class_='company-list-item')

    i = 0
    for li in li_arr:
        company = li.find('a', class_='list-item-title-text')           #获取class值为:list-item-title-text 的a标签
        address = li.find('a', class_='sm-offerResult-areaaddress')     #获取class值为:sm-offerResult-areaaddress 的a标签
        data = [company.get('title'), company.get('href'), address.get('title')]    #获取a标签中的值使用get('title')
        # data = data + reqUrl(company.get('href'))
        reqUrl(company.get('href'), i)
        i += 1
        # writeCsv(data)

"""
进入到公司主页,拿到联系方式的html
"""
def reqUrl(url, i):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Referer' : 'https://sanyinglighting.1688.com/',
        'Connection': 'keep-alive',
        'cookie': 'cna=I+agE08sdxsCAd/fyfQZ6zlX; __last_loginid__=19%E9%AD%94%E7%AC%9B19; lid=19%E9%AD%94%E7%AC%9B19; ali_apache_track=c_mid=b2b-27547022471d5e9|c_lid=19%E9%AD%94%E7%AC%9B19|c_ms=1; _cn_slid_=BeyyK7xw1z; UM_distinctid=16795d83ac763-00d4b6ee152a12-b79183d-1fa400-16795d83ac8e17; hng=CN%7Czh-CN%7CCNY%7C156; ali_ab=27.189.229.22.1544793403355.7; h_keys="LED%u706f#led"; ali_beacon_id=27.189.219.110.1544857160141.831344.0; alisw=swIs1200%3D1%7C; last_mid=b2b-27547022471d5e9; cookie2=108aa0adfd4ded876370e8ab628cd95b; t=0484afe62312125dc63df2a83e07fd6a; _tb_token_=ebe40beea1fb3; __cn_logon__=true; __cn_logon_id__=19%E9%AD%94%E7%AC%9B19; ali_apache_tracktmp=c_w_signed=Y; __rn_alert__=false; cookie1=BxE2%2BYxY4XJP6iktIgQQl6LqeAJ%2F0qjz2WLiATMIVWI%3D; cookie17=UU8NZRSjhEy3vw%3D%3D; sg=972; csg=92a6e324; unb=2754702247; _nk_=19%5Cu9B54%5Cu7B1B19; _csrf_token=1545917429101; _is_show_loginId_change_block_=b2b-27547022471d5e9_false; _show_force_unbind_div_=b2b-27547022471d5e9_false; _show_sys_unbind_div_=b2b-27547022471d5e9_false; _show_user_unbind_div_=b2b-27547022471d5e9_false; alicnweb=touch_tb_at%3D1545921296265%7ChomeIdttS%3D73863002145434246959440807833300929548%7ChomeIdttSAction%3Dtrue%7Clastlogonid%3D19%25E9%25AD%2594%25E7%25AC%259B19%7Cshow_inter_tips%3Dfalse; ad_prefer="2018/12/27 22:35:38"; l=aBZTI4SiyiOyXIBo2Ma4HVRas707A2ZPVwnE1MakfTEhNnzS8XUYx5ro-VwWT_qC5Jvy_K-5Z; isg=BJKSQWv1GgkbK2FLrO7cqhT241i0C4l3-ath8lzrosUwbzJpRDJcTLqN24t2GA7V'
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    contactinfo = soup.find('li', class_='contactinfo-page')
    consUrl = contactinfo.find('a').get('href')
    return getPhoneNumber(consUrl, i)


"""
获取公司联系方式
"""
def getPhoneNumber(url, i):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        # 'Referer': 'https://sanyinglighting.1688.com/',
        'Connection': 'keep-alive',
        'cookie': 'cna=I+agE08sdxsCAd/fyfQZ6zlX; __last_loginid__=19%E9%AD%94%E7%AC%9B19; lid=19%E9%AD%94%E7%AC%9B19; ali_apache_track=c_mid=b2b-27547022471d5e9|c_lid=19%E9%AD%94%E7%AC%9B19|c_ms=1; _cn_slid_=BeyyK7xw1z; UM_distinctid=16795d83ac763-00d4b6ee152a12-b79183d-1fa400-16795d83ac8e17; hng=CN%7Czh-CN%7CCNY%7C156; ali_ab=27.189.229.22.1544793403355.7; h_keys="LED%u706f#led"; ali_beacon_id=27.189.219.110.1544857160141.831344.0; alisw=swIs1200%3D1%7C; last_mid=b2b-27547022471d5e9; cookie2=108aa0adfd4ded876370e8ab628cd95b; t=0484afe62312125dc63df2a83e07fd6a; _tb_token_=ebe40beea1fb3; __cn_logon__=true; __cn_logon_id__=19%E9%AD%94%E7%AC%9B19; ali_apache_tracktmp=c_w_signed=Y; __rn_alert__=false; cookie1=BxE2%2BYxY4XJP6iktIgQQl6LqeAJ%2F0qjz2WLiATMIVWI%3D; cookie17=UU8NZRSjhEy3vw%3D%3D; sg=972; csg=92a6e324; unb=2754702247; _nk_=19%5Cu9B54%5Cu7B1B19; _csrf_token=1545917429101; _is_show_loginId_change_block_=b2b-27547022471d5e9_false; _show_force_unbind_div_=b2b-27547022471d5e9_false; _show_sys_unbind_div_=b2b-27547022471d5e9_false; _show_user_unbind_div_=b2b-27547022471d5e9_false; alicnweb=touch_tb_at%3D1545921296265%7ChomeIdttS%3D73863002145434246959440807833300929548%7ChomeIdttSAction%3Dtrue%7Clastlogonid%3D19%25E9%25AD%2594%25E7%25AC%259B19%7Cshow_inter_tips%3Dfalse; ad_prefer="2018/12/27 22:35:38"; l=aBZTI4SiyiOyXIBo2Ma4HVRas707A2ZPVwnE1MakfTEhNnzS8XUYx5ro-VwWT_qC5Jvy_K-5Z; isg=BJKSQWv1GgkbK2FLrO7cqhT241i0C4l3-ath8lzrosUwbzJpRDJcTLqN24t2GA7V'
    }
    res = requests.get(url, headers=headers)
    html = res.text
    filename = 'E:\\html1\\html_' + str(i) + '.txt'

    with open(filename, 'w') as fileobject:  # 使用‘w’来提醒python用写入的方式打开
        fileobject.write(html)
    # soup = BeautifulSoup(res.text, 'html.parser')
    # div = soup.find('div', class_='contcat-desc')
    # contcat_arr = div.find_all('dl')
    # i = 1
    # data = []
    # for contact in contcat_arr:
    #     data.append(contact.find('dd').text.rstrip().strip('                                                    '))
    #     i += 1
    #     if i > 3:
    #         break
    # return data


'''写入数据到csv中'''
def writeCsv(data):
    print(data)
    flag = os.path.exists('E:\write.csv')   #文件是否存在
    with open('E:\write.csv', 'a', newline='') as csv_file:     #a是追加
        if flag :
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data)
        else:   #一开始不存在则写入表头
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['公司名称', '淘宝地址', '公司办公地址', '电话', '手机号', '传真'])


if __name__ == '__main__':
    readHtml('E:\html')