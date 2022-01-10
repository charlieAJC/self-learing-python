from bs4 import BeautifulSoup
import requests
import pandas as pd
import itertools
import datetime
import sys
sys.path.append("..")
import database.database as database  # noqa


class yahoo:
    today_date = ''
    today_datetime = ''

    # {Function 建構式}
    def __init__(self):
        self.today_date = datetime.datetime.now().strftime('%Y-%m-%d')
        self.today_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # {Function 紀錄上市股票漲幅排行}
    # {Return bool 是否紀錄成功}
    def record_change_up() -> bool:
        url = 'https://tw.stock.yahoo.com/rank/change-up?exchange=TAI'
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        change_up_html = soup.select('li.List\(n\) > div')
        # stock_data 預期格式
        # [
        #     [名次, 股名, 股號, 成交價, 漲跌, 漲跌幅, 最高, 最低, 價差, 成交量(張), 成交值(億)],
        #     ['1', '瑞利', '1512.TW', '5.39', '0.49', '10.00%', '5.39', '4.91', '0.48', '753', '0.0397'],
        #     ['2', '業旺', '1475.TW', '56.10', '5.10', '10.00%', '56.10', '52.00', '4.10', '301', '0.1669']
        # ]
        #
        stock_data = []
        times = 1
        for data in change_up_html:
            # stripped_strings 參考資料：https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#get-text
            stock_data.append([text for text in data.stripped_strings])
            times += 1
            if times > 10:
                break
