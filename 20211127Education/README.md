# Python網路爬蟲與數據工程師技術班 #

[在職訓練網 課程資訊](https://ojt.wda.gov.tw/ClassSearch/Detail?OCID=136398&plantype=1)

### 新知軟體及套件 ###

* YFinance & Yahoo! Finance API:雅虎財經API
* kendo:jquery套件，將資料轉換成 table 更加簡易化，但是要付費
* multicharts:程式交易操盤軟體

### vscode 安裝 python autopep8 auto formatter ###
1. 在 vscode 設定中搜尋 `python.formatting.provider` ，確定設定為 `autopep8`
2. 在 vscode 設定檔 settings.json 中加入以下程式碼(注意:請確定 `auto save` 須為 `off` )
    ```
    "[python]": {
        "editor.formatOnSave": true
    },
    ```
3. 隨便找個 python 檔儲存，如果沒有安裝 `autopep8` 則 vscode 會提醒是否要安裝
    * 或者直接在 command line 中安裝 `autopep8`
        ```
        python -m pip install -U autopep8
        ```

### 課程內容 ###

* 1128
    * 1: 運算符號、比較符號、變數型態、型態轉換
    * 2: if 判斷
    * 3: array, tuple, dictionary 型態操作
    * 4: for 迴圈
    * 5: input(), while 迴圈, try except 例外處理
* 1205
    * 1: 
* 1212
    * request 取得資料，用 beautiful soup 分析靜態資料，或分析從 api 取得的 json
* 1219
    * 1: 將爬蟲取得的資料存成方便寫入 database 的格式
    * 2: 連線資料庫
    * 3: 將 1 & 2 的程式整合
    * @todo:優化 sql 不要爬到一篇文章就 insert 一次，連線功能模組化
    * @todo:當資料存在時不要 insert ，參考資料:https://stackoverflow.com/questions/2366813/on-duplicate-key-ignore
    * sql 匯出:C:\xampp\mysql\bin\mysqldump -u user -puser mdu newsdata > C:\Users\user\Desktop\backup.sql
    * sql 匯入:mysql -u Username -p DatabaseName < Backup.sql
    * 4: 抓取靜態網頁資料，以 histock 抓取股票資訊
    * 5: 破解防爬蟲網頁
* 1226
    * 1: regex
    * 2: 範例:輸入密碼檢查格式
    * 3: regex取非json格式的資料，範例:中央氣象局各縣市天氣預報頁面
    * 4: 範例:日期為今天，取得指定格式的氣象資訊
    * 5: 排程執行程式
    * 6: request 加入特定 headers 已通過網站驗證，範例: ptt 八卦版的 18 歲驗證
    * 7: regex 的特殊用法:取有斷行的文章