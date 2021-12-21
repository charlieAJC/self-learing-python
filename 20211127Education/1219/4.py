import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://histock.tw/stock/2330"
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')

data = soup.select('table.tb-stock.tbPerform')
data1 = str(data[0])

# 由於一個 html 裡不一定只有一個表格，所以 pd.read_html(data1) 回傳型態會是陣列
data2 = pd.read_html(data1)
# data2[0].values 取得的是 NumPy object array
data3 = data2[0].values.tolist()
print(data3)
# @todo 將 台積電 (2330)近期表現 台積電 (2330)融資融券與借券 台積電 (2330)券商分點績效 的表單爬進來後寫進資料庫
# 並觀察資訊更新的頻率

# -------------------------------------------------------------

html = '<table class="tb-stock tbPerform"><tbody><tr><th class="lft w1 w33p">區間</th><th class="alt w1 w33p">                台積電</th><th class="alt2 w1 w33p">大盤</th></tr><tr class="alt-row"><th class="lft">三日</th><td><span class="clr-gr">-1.3%</span></td><td><span class="color:black">0%</span></td></tr><tr><th class="lft alt">一週</th><td><span class="clr-gr">-0.3%</span></td><td><span class="clr-rd">+1.1%</span></td></tr><tr class="alt-row"><th class="lft">兩週</th><td><span class="clr-gr">-1.6%</span></td><td><span class="color:black">0%</span></td></tr><tr><th class="lft alt">本月</th><td><span class="clr-gr">-0.5%</span></td><td><span class="clr-rd">+1.2%</span></td></tr><tr class="alt-row"><th class="lft">一個月</th><td><span class="clr-gr">-2.9%</span></td><td><span class="clr-gr">-0.1%</span></td></tr><tr><th class="lft alt">一季</th><td><span class="clr-rd">+1.9%</span></td><td><span class="clr-rd">+5.1%</span></td></tr><tr class="alt-row"><th class="lft">半年</th><td><span class="clr-rd">+2.4%</span></td><td><span class="clr-rd">+4.3%</span></td></tr><tr><th class="lft alt">今年</th><td><span class="clr-rd">+11.4%</span></td><td><span class="clr-rd">+19.4%</span></td></tr><tr class="alt-row"><th class="lft">一年</th><td><span class="clr-rd">+15.7%</span></td><td><span class="clr-rd">+23.7%</span></td></tr><tr><th class="lft alt f13">自今年高點</th><td><span class="clr-gr">-12.1%</span></td><td><span class="clr-gr">-1.4%</span></td></tr><tr class="alt-row"><th class="lft f13">自今年低點</th><td><span class="clr-rd">+18%</span></td><td><span class="clr-rd">+25.9%</span></td></tr><tr><th class="lft alt">兩年</th><td><span class="clr-rd">+78.7%</span></td><td><span class="clr-rd">+48%</span></td></tr><tr class="alt-row"><th class="lft">三年</th><td><span class="clr-gr">-0.2%</span></td><td><span class="clr-rd">+0.7%</span></td></tr><tr><th class="lft alt" style="width: 85px;">五年</th><td><span class="clr-gr">-1.3%</span></td><td><span class="color:black">0%</span></td></tr></tbody></table>'

list = pd.read_html(html)
# 取得個股的近期表現
tsmc_data = list[0].iloc[:, 1]
# 取得大盤的近期表現
market_data = list[0].iloc[:, 2]
