import requests
import json
import time

date_deadline = "2021-12-15"
keywords = ["香蕉", "梨子"]
newslists = []

for keyword in keywords:
    page_num = 1
    search = True
    while search:
        url = "https://udn.com/api/more?page={}&id=search:{}&channelId=2&type=searchword&last_page=352".\
            format(page_num, keyword)
        page = requests.get(url)
        if page.status_code != 200:
            print("請求失敗{}: url={} ".format(page.status_code, url))
        else:
            page = page.text
        x = json.loads(page)
        for i in x['lists']:
            news = {
                'title': i['title'],
                'link': i['titleLink'],
                'data': i['time']['date'][:10]
            }
            newslists.append(news)
            article_date = i['time']['date'][:10]
            now = time.strptime(article_date, "%Y-%m-%d")
            deadline = time.strptime(date_deadline, "%Y-%m-%d")
            if now < deadline:
                search = False
                break
        page_num = page_num + 1  # page_num +=1
