import re
import requests

# https://www.cwb.gov.tw/V8/C/W/County/index.html 中央氣象局各縣市天氣預報
url = 'https://www.cwb.gov.tw/Data/js/week/TableData_Week_County_C.js'

html = requests.get(url)
html.encoding = 'utf8'
page = html.text

# pattern = r"'(\d+)':["
pattern = r"\'(\d+)\'\:\["
cityNo = re.findall(pattern, page)
print(cityNo)

# 'date':'2021/12/26','time':'12:00','Temp':{'C':{'L':'13','H':'13'}
patn = "\'date\'\:\'2021/12/26\'\,\'time\'\:\'12\:00\'\,\'Temp\'\:\{\'C\'\:\{(.+?)\}"
temp = re.findall(patn, page)

# 取得特定日期的最高溫和最低溫
date = '2021/12/27'
# patn=r"\'date\'\:\'"+date+"\'\,\'time\'\:\'12\:00\'\,\'Temp\'\:\{\'C\'\:\{(.+?)\}"
# patn=r"\'date\'\:\'"+date+"\'\,\'time\'\:\'\d+\:\d+\'\,\'Temp\'\:\{\'C\'\:\{(.+?)\}"
patn = r"\'date\'\:\'" + date + "'.+\'L\'\:\'(\d+).+H\'\:\'(\d+).+,\'F\'"
temp = re.findall(patn, page)

# 用這個檔案組成 [[cityNo1, 縣市名1], [cityNo2, 縣市名2]...]
url = "https://www.cwb.gov.tw/Data/js/info/Info_County.js"
html1 = requests.get(url)
html1.encoding = 'utf8'
page1 = html1.text
patn = r"\'ID\':\'(\d+)\'.+\'C\':\'(\w+)\'"
cityPair = re.findall(patn, page1)
