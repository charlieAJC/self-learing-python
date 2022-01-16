import requests
from bs4 import BeautifulSoup

# 創造一個 session 連線
session = requests.session()

# 取得登入頁面，並取出頁面裡的 csrf_key
login_url = 'http://hsf.asuscomm.com/memberLogin/'
login_response = session.get(login_url)
login_page = login_response.text
login_headers = login_response.headers
login_cookies = session.cookies.get_dict()

login_soup = BeautifulSoup(login_page, 'lxml')
# csrf_key = login_soup.select('input[name=csrfmiddlewaretoken]')[0]['value']
csrf_key = login_soup.select_one(
    'input[name=csrfmiddlewaretoken]').get('value')

# 以帳號、密碼、csrf_key 連線登入網址
# 老師的網頁沒有檢查 headers，一般都需要帶
headers = {
    # 'Cookie': 'csrftoken={}'.format(re.findall(r"csrftoken=(\w+);", login_headers['Set-Cookie'])[0])
}

payload = {
    'csrfmiddlewaretoken': csrf_key,
    'account': 'hsfncu',
    'password': 'hsfhsf44'
}

cookies = {
    'csrftoken': login_cookies['csrftoken']
}

login2_response = session.post(
    login_url,
    payload,
    cookies=cookies,
    headers=headers
)

# 取登入回應 header 中的 sessionid
login2_cookies = session.cookies.get_dict()

# 第三次連線 登入後的網址
lobby_url = 'http://hsf.asuscomm.com/memberSearch/'
lobby_html = session.get(
    lobby_url,
    cookies=login2_cookies
).text
