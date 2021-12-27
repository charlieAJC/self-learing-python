import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

# headers 視狀況帶，基本要帶的是 user-agent ，但ptt沒有檢查
# headers = {}
cookies = {'over18': '1'}

page = requests.get(url, cookies=cookies).text
soup = BeautifulSoup(page, 'lxml')

# 取得文章標題
title = soup.select('.r-ent .title a')
for i in title:
    print(i.text)

# 取得文章作者
author = soup.select('.r-ent .meta .author')
for i in author:
    print(i.text)

# @todo:作者跟標題一起取
