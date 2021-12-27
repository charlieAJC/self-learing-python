import requests
from bs4 import BeautifulSoup
import pandas as pd
import itertools


# 爬蟲取得 histock 個股資訊
class histock:
    histock_url = "https://histock.tw/stock/{}"
    # 股票代號
    stock_symbol = ''
    soup = ''

    # 建構式
    def __init__(self, stock_symbol: str):
        self.stock_symbol = stock_symbol
        self.histock_url = self.histock_url.format(self.stock_symbol)
        self.soup = BeautifulSoup(requests.get(self.histock_url).text, 'lxml')

    # {Function 取得大盤和各股的近期表現}
    # {Return list [個股近期表現, 大盤近期表現]}
    def get_performance(self) -> list:
        html_table = str(self.soup.select('table.tb-stock.tbPerform')[0])
        pandas_table = pd.read_html(html_table)
        # 取得個股的近期表現
        single_data = pandas_table[0].iloc[:, 1].tolist()
        # 取得大盤的近期表現
        market_data = pandas_table[0].iloc[:, 2].tolist()

        data = ','.join([f"'{c}'" for c in single_data])
        # @todo 1. 改成 INSERT ... ON DUPLICATE KEY UPDATE id=id
        #       2. 時間用 python 方法生成
        sql = f"INSERT INTO `performance` VALUES (null,'2330',{data},'2021-12-26 01:30:00')"


tsmc = histock('2330')
tsmc.get_page_html()
