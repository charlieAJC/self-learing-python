from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
import time

web = webdriver.Chrome('C:/Users/Administrator/Desktop/chromedriver.exe')

url = 'https://isin.twse.com.tw/isin/class_i.jsp?kind=1'
web.get(url)
time.sleep(2)

market_select = web.find_element_by_css_selector('select[name=market]')
Select(market_select).select_by_value('1')
time.sleep(2)

issue_select = web.find_element_by_css_selector('select[name=issuetype]')
Select(issue_select).select_by_index(7)
time.sleep(2)

web.find_element_by_css_selector('input[type=button][value=確定]').click()
time.sleep(2)

soup = BeautifulSoup(web.page_source, 'lxml')
html_table = str(soup.select('table.h4')[0])
pandas_table = pd.read_html(html_table)[0]
# table 欄位名稱在 dataFrame 表格 index = 1 位置，將 dataFrame 欄位名稱套用 table 的
pandas_table.columns = pandas_table.iloc[0, :]
pandas_table = pandas_table.drop(index=[0])
wtf = pandas_table.iloc[:, [2, 3, 7]].to_dict('records')
# wtf 格式
# [
#     {
#         '有價證券代號': '0050',
#         '有價證券名稱': '元大台灣50',
#         '公開發行/上市(櫃)/發行日': '2003/06/30'
#     },
#     {
#         '有價證券代號': '0051',
#         '有價證券名稱': '元大中型100',
#         '公開發行/上市(櫃)/發行日': '2006/08/31'
#     }
# ]

web.close()
