# 給定一字串 以空格區分關鍵字 ex: '蘋果 mac apple'
# 給定一時間格式當片段(先後隨意) ex:'2021-11-01' '2021-12-01'
# 以給定的時間中較晚的當查詢截止日，查出所有現在至查詢截止日且提及關鍵字的文章
import time
import datetime
import json
import requests

# 檢查使用者輸入日期的格式
input_validate = "%Y-%m-%d"
# 是否還需要繼續查詢
search = True
# 字串裡的參數可以先挖空，等需要用時以 url.format(page, search) 的方法取得新字串
url = "https://udn.com/api/more?page={}&id=search:{}&channelId=2&type=searchword"


def get_legal_input(message, form):
    '''
    檢查使用者 input 的值是否符合格式
    '''
    while True:
        value = input(message)
        if form == 'date':
            global input_validate
            try:
                # 檢查日期格式，並轉成符合的格式(如:2021-2-5 -> 2021-02-05)
                value = datetime.datetime.strftime(
                    datetime.datetime.strptime(value, input_validate), input_validate)
                break
            except ValueError:
                print('請輸入正確的日期格式')
        elif form == 'string':
            if value == '':
                print('請輸入文字')
            else:
                break
    return value


def go_crawler(keyword_list, end_date):
    global url
    result = {}
    for keyword in keyword_list:
        page = 1
        keep_search = True
        result[keyword] = []
        while keep_search:
            search_url = url.format(page, keyword)
            response = requests.request('GET', search_url)
            if (response.status_code != 200):
                keep_search = False
                break
            else:
                data = json.loads(response.text)
                lists = data['lists']
                for list in lists:
                    if datetime.datetime.strptime(end_date, '%Y-%m-%d') <= datetime.datetime.strptime(list['time']['date'], '%Y-%m-%d %H:%M:%S'):
                        # 測試 dict key 是否存在的方法
                        # if keyword in result
                        result[keyword].append({
                            'title': list['title'],
                            'link': list['titleLink'],
                            'cateTitle': list['cateTitle'],
                            'time': list['time']['date']
                        })
                    else:
                        keep_search = False
                        break
                page += 1
            # sleep() 避免陷入意外的無窮迴圈時 cpu 太快過載
            time.sleep(0.2)
    return result


# step1. 要求使用者輸入符合格式的資訊
keyword = get_legal_input('請輸入要查詢的關鍵字: ', 'string')
first_date = get_legal_input('請輸入日期一: ', 'date')
second_date = get_legal_input('請輸入日期二: ', 'date')

# step2. 排序輸入日期成 開始查詢及結束查詢日期
# 注意 sort() 和 sorted() 的用法
# sort() 是方法，用法是 list.sort()，改變的是 list 本身
# sorted() 是函數，用法是 sorted(list)，list 本身並無改變
start_date, end_date = sorted([first_date, second_date])

# step3. 爬蟲取資料
# 將關鍵字串以空白分割
keyword_list = keyword.split()
# 開爬!
crawler = go_crawler(keyword_list, end_date)
print(json.dumps(crawler))

# Python中time和datetime的区别与联系
# https://blog.csdn.net/haox0/article/details/102741483
# ------ 問題 ------
# function 註解怎麼寫? -> https://www.askpython.com/python/python-comments
# 一個檔案的順序? 常數->function
# pep8的斷行機制
# 如果 sorted(list) 不接值，記憶體裡面會怎麼記錄這個參數，他就沒有 key 耶?
# 什麼狀況下才會在爬蟲時就爬取特定時間區間的資料?
# 布署建議
# function 模組化
# ------ 問題 ------
