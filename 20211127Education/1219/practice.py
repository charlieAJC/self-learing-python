import requests
from bs4 import BeautifulSoup
import pandas as pd
import itertools

url = "https://histock.tw/stock/2330"
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')

# part1. 近期表現
html_table = str(soup.select('table.tb-stock.tbPerform')[0])
pandas_table = pd.read_html(html_table)
# 取得個股的近期表現
# ['-1.3%', '-0.3%', '-1.6%', '-0.5%', '-2.9%', '+1.9%', '+2.4%', '+11.4%', '+15.7%', '-12.1%', '+18%', '+78.7%', '-0.2%', '-1.3%']
tsmc_data = pandas_table[0].iloc[:, 1].tolist()
# 取得大盤的近期表現
market_data = pandas_table[0].iloc[:, 2].tolist()

# part2. 券商分點績效
html_table = str(soup.select('table.tbTable.tb-stock.tbChip')[0])
pandas_table = pd.read_html(html_table)
# [['台灣摩根士丹利', '0.13%', 1192.3, 903, 598.7], ['美商高盛', '0.09%', 584.2, 892, 599.0], ['美林', '0.03%', 334.0, 1160, 599.4], ['凱基-台北', '0.15%', 268.0, 157, 598.6], ['港商法國興業', '0.23%', 166.0, 109, 598.4], ['花旗環球', '0.12%', 158.5, 200, 599.1], ['兆豐-新竹', '0.31%', 84.4, 44, 598.2], ['富邦', '0.01%', 59.1, -1073, 599.9], ['兆豐-忠孝', '0.16%', 57.0, 59, 599.0], ['大和國泰', '0.20%', 53.0, 35, 598.8]]
performance_table = pandas_table[0].iloc[:, 1:].values.tolist()

# part3. 融資融券與借券
html_table = str(soup.select('div#LBlock_8 table.tb-stock.tbChip')[0])
pandas_table = pd.read_html(html_table)
securities_data = pandas_table[0].iloc[[0, 2, 4, 6]].values.tolist()
# ['-367', '-3', '-161', '0', '0.00%', '24743', '65', '14787', '646', '301620', '2', '163', '32602', '0.26%', '6482595', '1091', '11.12%', '124.66', nan, nan]
# @todo list 裡面的 nan 拿掉
print(list(itertools.chain.from_iterable(securities_data)))
