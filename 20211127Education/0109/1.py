# 1. 安裝 Selenium:pip install selenium
# 2. 安裝瀏覽器驅動程式
# 2-1. 在瀏覽器的說明中檢查瀏覽器版本號碼(以下以 chrome 為例)
# 2-2. 在網路上(https://chromedriver.chromium.org/downloads)下載版本號碼對應的瀏覽器驅動程式
#      firefox driver 可以在 mozilla 的 github 上下載，相較 chrome driver 需找第三方較值得信賴

# 補充:Selenium 幾乎可以取 99% 的網站資料，老師碰到的例外是:玩股網
from selenium import webdriver

# 設定 chrome 內部參數 的方法
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# 關閉聲音
# chrome_options.add_argument('--mute-audio')
# 無頭模式，不顯示chrome視窗，但會背景執行
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome('driver/chromedriver.exe', options=chrome_options)

web = webdriver.Chrome('C:/Users/Administrator/Desktop/chromedriver.exe')
# 以下為 firefox 驅動方法，與 chrome 稍微不同
# webdriver.Firefox(executable_path="C:/Users/user/Desktop/geckodriver.exe")

# web.set_window_position(480,0)
# web.set_window_size(400,400)
# web.maximize_window()

keyword = 'MacBook'
page = 1
url = "https://www.momoshop.com.tw/search/searchShop.jsp" + \
    "?keyword={}&searchType=1&cateLevel=0&cateCode=&curPage={}&_isFuzzy=0&showType=chessboardType" . \
    format(keyword, page)
# 網址連線
web.get(url)

# 取得商品名稱
prdTitles = web.find_elements_by_css_selector("h3.prdName")
prdTitle = []
for i in prdTitles:
    prdTitle.append(i.text)
    # print(i.text)

# 取得商品價格
prdPrices = web.find_elements_by_css_selector("span.price > b")
prdPrice = []
for i in prdPrices:
    prdPrice.append(i.text.replace(',', ''))
    # print(i.text)

products = []
for i in range(len(prdTitle)):
    products.append({'title': prdTitle[i], 'price': prdPrice[i]})

# 完成程序，關閉瀏覽器視窗
web.close()
