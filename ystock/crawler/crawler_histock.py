from database.database import run_sql
from bs4 import BeautifulSoup
import requests
import pandas as pd
import itertools
import datetime
# import database
# from database import run_sql
import sys
sys.path.insert(0, '..')


# 爬蟲取得 histock 個股資訊
class histock:
    histock_url = "https://histock.tw/stock/{}"
    # 股票代號
    stock_symbol = ''
    soup = ''

    # {Function 建構式}
    # {Input stock_symbol {string} 股票代號}
    def __init__(self, stock_symbol: str):
        self.stock_symbol = stock_symbol
        self.histock_url = self.histock_url.format(self.stock_symbol)
        self.soup = BeautifulSoup(requests.get(self.histock_url).text, 'lxml')

    # {Function 紀錄大盤和各股的近期表現}
    # {Return bool 是否紀錄成功}
    def record_performance(self) -> bool:
        html_table = str(self.soup.select('table.tb-stock.tbPerform')[0])
        pandas_table = pd.read_html(html_table)
        # 取得個股的近期表現
        single_data = pandas_table[0].iloc[:, 1].tolist()
        # 取得大盤的近期表現
        market_data = pandas_table[0].iloc[:, 2].tolist()

        today_date = datetime.datetime.now().strftime('%Y-%m-%d')
        today_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        single_string = ','.join(
            [f"{c.replace('%', '')}" for c in single_data])
        market_string = ','.join(
            [f"{c.replace('%', '')}" for c in market_data])
        # 使用 INSERT ... ON DUPLICATE KEY UPDATE 避免資料重複更新
        # 大盤股票代號設定為 0
        sql = f"INSERT INTO `stock_performance` VALUES " + \
            f"(null,'{self.stock_symbol}','{today_date}',{single_string},'{today_datetime}','{today_datetime}')," + \
            f"(null,'0','{today_date}',{market_string},'{today_datetime}','{today_datetime}') " + \
            f"ON DUPLICATE KEY UPDATE id=id"
        # result = database.run_sql(sql)
        result = run_sql(sql)
        if (result):
            print('success')
        else:
            print('fail')
