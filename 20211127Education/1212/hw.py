# 給定一字串 以空格區分關鍵字 ex: '蘋果 mac apple'
# 給定二時間格式當片段(先後隨意) ex:'2021-11-01' '2021-12-01'
# 查出所有關聯文章
# 可以用 sleep(0.2) 讓意外的無窮迴圈不會讓 cpu 壞掉 (需要 import time)
# import time
# time.sleep(0.2)

# import requests
import time

# 可提供 input 的參數
keyword = 'mac 優惠 apple'
# first_date = '2021-12-12'
# second_date = '2021-12-01'
first_date = input('請輸入日期一: ')
second_date = input('請輸入日期二: ')

# 查詢日期區間的開始日期
start_date = ''
# 查詢日期區間的結束日期
end_date = ''
# 檢查使用者輸入日期的格式
input_validate = "%Y-%m-%d"
# 是否還需要繼續查詢
search = True

# def validate_input_date():


def sort_date():
    '''
    將使用者輸入的日期參數 first_date & second_date 排序後
    賦值給日期參數 start_date & end_date
    '''
    global first_date, second_date, start_date, end_date
    sort_array = [first_date, second_date]
    sort_array.sort()
    # 批量賦值(assign value)的方法
    start_date, end_date = sort_array
    print(start_date)
    print(end_date)


sort_date()
