import os
import pandas as pd
import requests
import json
import time
import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    user='learnPython',
    password='justaproject',
    db='learn_python',
    charset='utf8'
)
cursor = db.cursor()
date_deadline = "2021-12-18"
keywords = ["新冠肺炎"]
newslists = []
for keyword in keywords:
    page_num = 1
    search = True
    while search:
        # 可以寫成
        # payload = {'page': '1', 'id': 'search:mac'}
        # url = 'https://udn.com/api/more'
        # request.get(url, params = payload)
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
            sql = "select * from newsdata where title='{}'".format(i['title'])
            cursor.execute(sql)
            db.commit()
            data = cursor.fetchall()
            if len(data) == 0:  # 資料庫內找不到舊資料，個數為0， 則新增入資料庫
                sql = "INSERT INTO newsdata (title,link,time) values ('{}','{}','{}')".\
                    format(i['title'], i['titleLink'], i['time']['date'][:10])
                cursor.execute(sql)
                db.commit()
                print("資料儲存: {}".format(i['title'][:10]))
            else:
                print("資料已存在: {}，skip".format(i['title'][:10]))
            article_date = i['time']['date'][:10]
            now = time.strptime(article_date, "%Y-%m-%d")
            deadline = time.strptime(date_deadline, "%Y-%m-%d")
            if now < deadline:
                search = False
                break
        print(page_num, article_date)
        page_num = page_num+1  # page_num +=1
db.close()


# @todo:將爬蟲資料匯出成 excel 檔案
# 如果檔案太大就不適合用這個方法，需用 python open data 寫入
# 參考:https://www.runoob.com/python/python-func-open.html

if os.path.isfile("C:/Users/user/Desktop/news.xls"):
    input_DF = pd.read_excel("C:/Users/user/Desktop/news.xls")
    input_DF = input_DF.drop(columns=[input_DF.columns[0]])
    output_DF = pd.DataFrame(newslists)
    output_DF = pd.concat([input_DF, output_DF], axis=0, ignore_index=True)
else:
    output_DF = pd.DataFrame(newslists)
output_DF.to_excel("C:/Users/user/Desktop/news.xls")
