import pymysql


class database_operation:

    def run_sql(sql):
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
        try:
            # 執行語法
            cursor.execute(sql)
            # 提交修改
            db.commit()
            # 取得查詢結果(資料型態是 tuple，是一種不能改值的 list )
            # 注意取得到的資料如果帶有時間，它的型態會是 datetime.date(2021, 12, 17)
            data = cursor.fetchall()
        except:
            # 發生錯誤時停止執行SQL
            db.rollback()
            data = False

        db.close()
        return data
