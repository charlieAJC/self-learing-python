from selenium import webdriver
import time

web = webdriver.Chrome('C:/Users/Administrator/Desktop/chromedriver.exe')
# implicitly_wait 隱性等待
web.implicitly_wait(10)

url = 'http://hsf.asuscomm.com/memberLogin/'
web.get(url)

web.find_element_by_name('account').send_keys('hsfncu')
web.find_element_by_name('password').send_keys('hsfhsf44')
time.sleep(1)
web.find_element_by_css_selector('input[type=submit]').click()

# url2="http://hsf.asuscomm.com/memberSearch/"
# web.get(url2)
