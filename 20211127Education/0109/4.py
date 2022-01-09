from selenium import webdriver
import time


web = webdriver.Chrome("C:/Users/Administrator/Desktop/chromedriver.exe")
web.implicitly_wait(10)

url1 = "http://hsf.asuscomm.com/memberLogin/"
web.get(url1)

web.find_elements_by_name("account")[0].send_keys("hsfncu")

web.find_elements_by_name("password")[0].send_keys("hsfhsf44")
x = web.find_elements_by_css_selector("form > p > input")[2].click()

# url2 = "http://hsf.asuscomm.com/memberAdmin/mdu/"
# web.get(url2)
# time.sleep(2)
# if web.find_elements_by_name("mua")[0].is_selected():
#     pass
# else:
#     web.find_elements_by_name("mua")[0].click()

url3 = "http://hsf.asuscomm.com/memberSearch/"
web.get(url3)
data = web.find_elements_by_name('searchAttribute')
time.sleep(2)
data[2].click()
