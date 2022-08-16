
import os
from urllib.request import *

print('ダウンロード開始')


dir = os.path.dirname(os.path.abspath(__file__)) + '/html/'

if not os.path.exists(dir): os.mkdir(dir)

url = 'https://shopping.yahoo.co.jp/search?view=list&p=%E8%AA%BF%E5%91%B3%E6%96%99&tab_ex=commerce&X=3&sc_i=shp_pc_search_sort_sortitem'

filepath = dir + '/shopping.yahoo.html'

urlretrieve(url, filepath)

print('ダウンロード完了')