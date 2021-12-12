import requests
from bs4 import BeautifulSoup

url = "https://udn.com/search/word/2/macbook"
page = requests.get(url)

if page.status_code != 200:
    # {}:將 format() 中的參數依序放入字串中的大括號裡
    # 參考資料:https://medium.com/tsungs-blog/python-%E5%AD%97%E4%B8%B2%E6%A0%BC%E5%BC%8F%E5%8C%96-fdfe4ac41a2d
    print("請求失敗{}: url={}".format(page.status_code, url))
else:
    page = page.text
    # 可能需要先在命令列安裝 lxml : pip install lxml
    soup = BeautifulSoup(page, 'lxml')
    # find_all() 可能會改變 html 標籤裡的屬性排序
    # 參考資料:https://www.v2ex.com/t/646203
    # tmp = soup.find_all('a')
    # tmp = soup.select('div.story-list__text > h2 > a')

    # 取得標題和連結
    # tmp = soup.select('div.story-list__text a[title]')
    # index = 0
    # for i in tmp:
    #     # get('href') 取標籤內的連結
    #     # getText() 取標籤夾的內容
    #     print(index, i.getText(), i.get('href'))
    #     index += 1

    # 取得文章時間
    tmp = soup.select('div.story-list__text .story-list__info time')
    index = 0
    for i in tmp:
        print(index, i.getText())
        index += 1

# 補充知識
# 轉換時間字串的格式 https://stackoverflow.com/questions/58231361/convert-local-timestamp-to-unix-epoch-timestamp-in-python
# 字串分割 string.split(分段文字)
