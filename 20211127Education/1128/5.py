# input()
# 從 input 取得的參數型態一定是 string
# 補充:print()也會將裡面的參數轉成 string 再輸出
# while 迴圈
# try except(catch) 錯誤處理，python 內建的例外(https://docs.python.org/zh-tw/3/library/exceptions.html)
while True:
    height = input('請輸入您的身高: ')
    try:
        print('加 10 公分為: ', int(height) + 10)
        break
    except ValueError:
        print('請勿輸入數字以外的值')
