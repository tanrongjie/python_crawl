import requests

"""读取阿里巴巴网站数据存入到txt文件中"""
def spider_taobao(url, num):
    headers = {
        'Accept':'application/json, text/plain, */*',
        'Accept-Language':'zh-CN,zh;q=0.3',
        'Referer':'https://s.1688.com/company/company_search.htm?keywords=LED%B5%C6&button_click=top&n=y&netType=1%2C11&smToken=91d2bd60f2f8464c84d631eab925c247&smSign=b0K7VTPI%2BuGNa6fmf8u33A%3D%3D',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Connection':'keep-alive',
        'cookie':'cna=I+agE08sdxsCAd/fyfQZ6zlX; __last_loginid__=19%E9%AD%94%E7%AC%9B19; last_mid=b2b-27547022471d5e9; lid=19%E9%AD%94%E7%AC%9B19; ali_apache_track=c_mid=b2b-27547022471d5e9|c_lid=19%E9%AD%94%E7%AC%9B19|c_ms=1; _cn_slid_=BeyyK7xw1z; UM_distinctid=16795d83ac763-00d4b6ee152a12-b79183d-1fa400-16795d83ac8e17; hng=CN%7Czh-CN%7CCNY%7C156; ali_ab=27.189.229.22.1544793403355.7; cookie2=10491bd931d64ffca009079abe2a497f; t=0484afe62312125dc63df2a83e07fd6a; _tb_token_=e7beb79133703; alisw=swIs1200%3D1%7C; cookie1=BxE2%2BYxY4XJP6iktIgQQl6LqeAJ%2F0qjz2WLiATMIVWI%3D; cookie17=UU8NZRSjhEy3vw%3D%3D; sg=972; csg=0942638c; unb=2754702247; __cn_logon__=true; __cn_logon_id__=19%E9%AD%94%E7%AC%9B19; ali_apache_tracktmp=c_w_signed=Y; _nk_=19%5Cu9B54%5Cu7B1B19; _csrf_token=1544796019452; __rn_alert__=false; h_keys="LED%u706f#led"; alicnweb=touch_tb_at%3D1544802980835%7ChomeIdttS%3D73863002145434246959440807833300929548%7ChomeIdttSAction%3Dtrue%7Clastlogonid%3D19%25E9%25AD%2594%25E7%25AC%259B19%7Cshow_inter_tips%3Dfalse; _is_show_loginId_change_block_=b2b-27547022471d5e9_false; _show_force_unbind_div_=b2b-27547022471d5e9_false; _show_sys_unbind_div_=b2b-27547022471d5e9_false; _show_user_unbind_div_=b2b-27547022471d5e9_false; ad_prefer="2018/12/15 00:03:31"; isg=BM3NEAChrb8v3Q6aX7dLizef3OmHAh42utKOww9SAmTTBu241_n1TaiUdNrFxhk0'
    }

    try:
        res = requests.get(url, headers=headers)
    except Exception as e:
        print('无法打开网页:'+ e.reason)

    try:
        html = res.text
        filename = 'E:\\html\\html_' + str(num) + '.txt'

        with open(filename, 'w') as fileobject:  # 使用‘w’来提醒python用写入的方式打开
            fileobject.write(html)
        # for item in items:
        #     print(items[0], items[1])
    except Exception as e:
        print('数据抽取失败!!!' + e.reason)

if __name__ == '__main__':
    for num in range(41, 51):
        url = 'https://s.1688.com/company/company_search.htm?keywords=LED%B5%C6&netType=1%2C11&button_click=top&n=y&pageSize=30&smToken=4e4ba594029d4f9f9ed5ff38dfc8013d&smSign=puAgc3T5YPqRnXOSVI2f1A%3D%3D&offset=3&beginPage=' + str(num)
        # print(url)
        spider_taobao(url, num)