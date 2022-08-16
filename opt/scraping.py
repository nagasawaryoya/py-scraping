import os
import csv
import re
import time
import requests
import urllib.robotparser
from bs4 import BeautifulSoup

URL = 'https://shopping.yahoo.co.jp/search?X=3&view=grid&p=%E8%AA%BF%E5%91%B3%E6%96%99&ss_first=1&tab_ex=commerce&sc_i=shp_pc_search_vwtype_btn&area=13&b=1&row_sum=8'

"""
スクレイピングしていいか確認。
"""
rp = urllib.robotparser.RobotFileParser()

rp.set_url(URL + 'robots.txt')
rp.read()

# クローリングへの指示書があるか
req_rate = rp.request_rate('*')
if req_rate is None:
    print('クローリングへの指示書なし。')

    # URLの取得が許可されているかを確認
    req_URL = rp.can_fetch('*', URL)
    if req_URL == True:
        print('URLの取得も許可されている。これよりスクレイピングを開始。')
    else:
        print('URLの取得が許可されていない。スクレイピングを中止。')
else:
    print('クローリングへの指示書あり。利用規約を要確認。')


"""
スクレイピング
"""

csv_dir = os.path.dirname(os.path.abspath(__file__)) + '/csv/shopping.yahoo/'
if not os.path.exists(csv_dir): os.mkdir(csv_dir)

rows = []
for i in range(1100):

    m = re.search(r'(?<=&b=)\d+', URL)

    if m is not None:
        current_url = re.sub(r'(?<=&b=)\d+', str(int(m.group(0)) + (i * 30)), URL)

        bs = BeautifulSoup(requests.get(current_url, timeout=10).text, 'html.parser')

        rows.extend(
            list(map(
                lambda item: [
                    item.select_one('._2EW-04-9Eayr').text,
                    item.select_one('div[data-postage-beacon]').text,
                    item.select_one('._2EW-04-9Eayr')['href']
                ],
                bs.find_all('li', class_='LoopList__item')
            ))
        )
        print('count: ' + str(i) + "\n")

        if i % 100 == 0:
            with open(csv_dir + 'tyomiryo.csv', 'a', encoding='utf-8') as f: 
                csv.writer(f, lineterminator='\n').writerows(rows)
                rows = []

        time.sleep(1)
