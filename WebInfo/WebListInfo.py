import re
import requests
from openpyxl import Workbook
from requests import RequestException


def get_one_list(page_number):
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,BI,2,'+ str(page_number) +'.html'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content.decode('gbk')
        else:
            return page_number
    except RequestException:
        return page_number

def parse_list_page(html):
    pattern = re.compile('<div class="el">.*?<p class="t1.*?<a target="_blank" title="(.*?)" '+
'href="(.*?)".*?<span class="t2">.*?title="(.*?)" href="(.*?)".*?<span class="t3">(.*?)</span>.*?'+
'<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>.*?</div>',re.S)
    items = re.findall(pattern, html)
    return items


def print_to_excel(items):
    wb = Workbook(write_only= True)
    sheet = wb.create_sheet(title= 'position_list',index= 1)
    for i in range(len(items)):
        sheet.append(items[i])
    wb.save(filename= '51JobInfo.xlsx')

def main():
    total_items = []
    flag = 0
    for i in range(108,135):
        html = get_one_list(i)
        if html == i:
            for flag in range(3):
                html = get_one_list(i)
                if html != i:
                    break
                else:
                    continue
            print(i) # 第i页数据有问题
            break
        items = parse_list_page(html)
        total_items.extend(items)
    print_to_excel(total_items)


if __name__ == '__main__':
    main()




