# 這是老師寫的版本
import requests
from bs4 import BeautifulSoup

# 創造一個session連線
session = requests.session()

# 第一次連線登入網址
url1 = "http://hsf.asuscomm.com/memberLogin/"
login_page = session.get(url1).text
soup = BeautifulSoup(login_page, 'lxml')
# 取得第一次連線登入網址 隱藏的 KEY
csrf_key = soup.select("input")[0].get("value")


headers = {
    "Set-Cookie": "sessionid=qgquc32w4qs1slzb6803iroukj7nps10",
}

data = {
    'csrfmiddlewaretoken': csrf_key,
    'account': 'hsfncu',
    'password': 'hsfhsf44',
}

cookies = {
    'sessionid': 'qgquc32w4qs1slzb6803iroukj7nps10',
    'csrftoken': csrf_key
}

# 第二次連線登入網址，填入 帳號、密碼、KEY
page2 = session.post(url1, data=data, cookies=cookies, headers=headers)
sessiocCookies = page2.cookies
cookie_t = requests.utils.dict_from_cookiejar(sessiocCookies)
page2 = page2.text

# 第三次連線 登入後的網址

url2 = "http://hsf.asuscomm.com/memberSearch/"
page3 = session.get(url2, cookies=cookies).text
