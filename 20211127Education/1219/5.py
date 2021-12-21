import requests
from bs4 import BeautifulSoup
import pandas as pd

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
url = 'https://www.wantgoo.com/stock/2330/major-investors/main-trend'
page = requests.get(url, headers=header).text
