# 老師過去班級做過的查詢爬蟲(程式碼有問題)
import requests
import pymysql
import time


def newsSearch(keywords, startDate="", endDate=""):
    if endDate != "" and startDate != "":
        print("搜尋範圍內日期的新聞")
    elif endDate == "" and startDate != "":
        print("搜尋從過去的某一日到最後一篇")
        date = "2050-12-31"  # 設定日期
        index = 1
        newsList = []
        print('starDate=', startDate)
        startDate = time.strptime(startDate, "%Y-%m-%d")
        while(True):
            print('date=', date)
            lastNewsDate = time.strptime(date, "%Y-%m-%d")

            if lastNewsDate < startDate:  # 目前是字串str，無法做日期比對
                break
            else:
                url = "https://udn.com/api/more?page=%7B%7D&id=search:%7B%7D&channelId=2&type=searchword&last_page=4490%22".format(
                    index, keywords)
                page = requests.get(url)

                if page.status_code in [200, 201, 202]:
                    print("連線成功，繼續找資料")
                    # print(page.text)
                    import json
                    data = json.loads(page.text)  # 將文字轉亂成變數，之後就方便取值
                    # 需要檢查是否仍有資料存在，自己加寫，這裡沒寫檢查的程式碼
                    newsLists = data['lists']

                    for i in newsLists:
                        newsList.append(
                            {'title': i['title'], 'link': i['titleLink'], 'date': i['time']['date'][:10]})
                        date = i['time']['date'][:10]
                        print('title=', i['title'], 'date=',
                              i['time']['date'][:10])
                        lastNewsDate = time.strptime(date, "%Y-%m-%d")
                        if lastNewsDate < startDate:  # 目前是字串str，無法做日期比對
                            break
                        else:
                            print("寫入資料庫或是顯示於介面")
            index += 1
    else:
        print("搜尋全部新聞")


newsSearch('新冠肺炎', startDate="2021-07-27", endDate="")
