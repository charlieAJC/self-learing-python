import requests
from bs4 import BeautifulSoup
import pandas as pd
import itertools
import datetime


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

        today_date = datetime.datetime.now().strftime('%Y-%m-%d')
        today_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        single_data = ['-1.3%', '-0.3%', '-1.6%', '-0.5%', '-2.9%', '+1.9%', '+2.4%',
                       '+11.4%', '+15.7%', '-12.1%', '+18%', '+78.7%', '-0.2%', '-1.3%']
        data = ','.join([f"{c.replace('%', '')}" for c in single_data])
        # @todo ON DUPLICATE KEY UPDATE 後面還要逐個欄位指定...
        sql = f"INSERT INTO `stock_performance` VALUES (null,'2330','{today_date}'," + \
            f"{data},'{today_datetime}','{today_datetime}') ON DUPLICATE KEY UPDATE id=id"


tsmc = histock('2330')
tsmc.get_page_html()
