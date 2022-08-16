import os
import csv
from bs4 import BeautifulSoup
from pprint import pprint

"""
実行前にhtmlファイルをダウンロードしてテストする。
"""

print('テスト開始')

html_dir = os.path.dirname(os.path.abspath(__file__)) + '/html/'
with open(html_dir + '/shopping.yahoo.html', encoding='utf-8') as f:
    bs = BeautifulSoup(f, 'html.parser')

    tl = list(map(
        lambda item: [
            item.select_one('._2EW-04-9Eayr').text,
            item.select_one('div[data-postage-beacon]').text,
            item.select_one('._2EW-04-9Eayr')['href']
        ],
        bs.find_all('li', class_='LoopList__item')
    ))

    csv_dir = os.path.dirname(os.path.abspath(__file__)) + '/csv/shopping.yahoo/'
    if not os.path.exists(csv_dir): os.mkdir(csv_dir)

    with open(csv_dir + 'lab.tyomiryo.csv', 'w', encoding='utf-8') as f: 
        csv.writer(f, lineterminator='\n').writerows(tl)

print('テスト終了')