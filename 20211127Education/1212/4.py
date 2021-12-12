# 取出指定時間以後的新聞
import requests
import json
import time

date_deadline = "2021-11-10"
keywords = ["香蕉", "梨子"]

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
        # print(x['lists'][0]['title'])
        for i in x['lists']:
            print(i['title'])
            print(i['titleLink'])
            print(i['time']['date'][:10])
            article_date = i['time']['date'][:10]
            now = time.strptime(article_date, "%Y-%m-%d")
            deadline = time.strptime(date_deadline, "%Y-%m-%d")
            if now < deadline:
                search = False
                break
        page_num = page_num+1  # page_num +=1
