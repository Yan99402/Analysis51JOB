# 职位信息
from typing import Dict, List, Any

import requests
from requests import RequestException
import re
import pymongo
import openpyxl
import pandas


def load_urls():
    wb = openpyxl.load_workbook('F:/python数据/51Job/51JobInfo.xlsx')
    list_data = wb['position_list'].values
    df_data = pandas.DataFrame(list_data)
    df_data.columns = df_data.iloc[0]
    df_data = df_data.drop(0)
    df_data.reset_index(drop=True)
    return list(df_data['url'])

def get_position_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return str(response.content.decode('gbk'))
        else:
            return url
    except RequestException:
        return url


def parse_one_position(html):
    pattern = re.compile('<div class="cn">.*?<h1 title=".*?">(.*?)<input.*?<span class="lname">(.*?)</span>'
        + '.*?<strong>(.*?)</strong>.*?<p class="msg ltype">(.*?)</p>.*?<div class="jtag inbox">(.*?)</div>'
        + '.*?<div class="bmsg job_msg inbox">(.*?)</div>', re.S)
    items = re.findall(pattern, html)
    if len(items) ==1:
        dict_item = {
                'position': items[0][0],
                'address': items[0][1],
                'salary': items[0][2],
                'company_tab': items[0][3],
                'free_tab': items[0][4],
                'detail': items[0][5]
            }
    else:
        dict_item = items
    return dict_item


def write_to_mongo(data):
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.python
    collection = db['51JobPositionDetail']
    collection.insert(data)


def main():
    urls = load_urls()
    items = []
    count = 1
    for url in urls:
        print(count)
        count += 1
        html = get_position_page(url)
        for i in range(3):
            if html[0:1] == '<':
                break
            else:
                html = get_position_page(url)
        if html[0:1] == '<':
            item = parse_one_position(html)
            if len(item) != 0:
                items.append(item)
            else:
                print(url)
        else:
            print(url)
    write_to_mongo(items)


if __name__ == '__main__':
    main()
