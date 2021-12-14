# 給定一字串 以空格區分關鍵字 ex: '蘋果 mac apple'
# 給定二時間格式當片段(先後隨意) ex:'2021-11-01' '2021-12-01'
# 查出所有關聯文章
# 可以用 sleep(0.2) 讓意外的無窮迴圈不會讓 cpu 壞掉 (需要 import time)
# import time
# time.sleep(0.2)

# import requests
import time
import datetime

# 檢查使用者輸入日期的格式
input_validate = "%Y-%m-%d"
# 是否還需要繼續查詢
search = True


def get_legal_input(message, form):
    ''' 檢查使用者 input 的值是否符合格式
    '''
    while True:
        value = input(message)
        if form == 'date':
            global input_validate
            try:
                time.strptime(value, input_validate)
                break
            except ValueError:
                print('請輸入正確的日期格式')
        elif form == 'string':
            if value == '':
                print('請輸入文字')
            else:
                break
    return value


# step1. 要求使用者輸入符合格式的資訊
keyword = get_legal_input('請輸入要查詢的關鍵字: ', 'string')
first_date = get_legal_input('請輸入日期一: ', 'date')
second_date = get_legal_input('請輸入日期二: ', 'date')

# step2. 排序輸入日期成 開始查詢及結束查詢日期
# 其實可以在 get_legal_input 檢查時間時就轉成符合的格式了(如:2021-12-5 -> 2021-12-05)
# 這邊直接 sort() 即可
dates = [datetime.datetime.strptime(ts, input_validate) for ts in [
    first_date, second_date]]
dates.sort()
start_date, end_date = [datetime.datetime.strftime(
    ts, input_validate) for ts in dates]


print('關鍵字: ', keyword)
print('開始日: ', start_date)
print('結束日: ', end_date)

# ------ 問題 ------
# function 註解怎麼寫?
# 一個檔案的順序? 常數->function
# pep8的斷行機制
# ------ 問題 ------
