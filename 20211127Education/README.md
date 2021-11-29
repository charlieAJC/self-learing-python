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