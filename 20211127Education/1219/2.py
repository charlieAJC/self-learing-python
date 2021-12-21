# 安裝 xampp 並啟動 Apache 及 MySQL
# command line 下指令安裝 pip install PyMySQL
# 在 http://localhost/phpmyadmin PMA 介面新增一個使用者
# account: learnPython  pw: justaproject
# pymysql官方文件:https://pymysql.readthedocs.io/en/latest/index.html
import pymysql

# 參考資料: https://ithelp.ithome.com.tw/articles/10207905
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='learnPython',
    password='justaproject',
    db='learn_python',
    charset='utf8'
)
# 建立操作游標
cursor = db.cursor()

# ---------- insert ----------
# SQL語法（查詢資料庫版本）
sql = "INSERT INTO newsdata (title, link, time) values ('c', 'cc', '2021-12-17')"
try:
    # 執行語法，回傳 1(int)，是影響欄位數嗎?
    cursor.execute(sql)
    # 提交修改，回傳 None
    db.commit()
    # insert 一樣可以 fetchall，會得到一個空的 tuple
    # print(cursor.fetchall())
except:
    # 發生錯誤時停止執行SQL
    db.rollback()
    print('error')
# ---------- insert ----------

# ---------- select ----------
# sql = "SELECT * FROM newsdata WHERE title = 'c' AND time >= '2021-12-18'"
# try:
#     # 執行語法
#     cursor.execute(sql)
#     # 提交修改
#     db.commit()
#     # 取得查詢結果(資料型態是 tuple，是一種不能改值的 list )
#     # 注意取得到的資料如果帶有時間，它的型態會是 datetime.date(2021, 12, 17)
#     data = cursor.fetchall()
#     print(data)
# except:
#     # 發生錯誤時停止執行SQL
#     db.rollback()
#     print('error')
# ---------- select ----------

# 關閉連線
db.close()
