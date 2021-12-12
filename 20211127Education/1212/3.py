# BeautifulSoup call api
import requests
import json

url = "https://udn.com/api/more?page=1&id=search:macbook&channelId=2&type=searchword&last_page=39"
page = requests.get(url)

if page.status_code != 200:
    print("請求失敗{}: url={}".format(page.status_code, url))
else:
    data = json.loads(page.text)
    for news_data in data['lists']:
        print(news_data['title'])
