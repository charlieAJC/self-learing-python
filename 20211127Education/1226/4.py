import re
import requests
# @homework: 日期為今天，利用兩個 url 檔案湊成 [
#   {'cityName':城市名稱, 'time':..., temp: {'low':..., 'high':...}}
# ]
url = "https://www.cwb.gov.tw/Data/js/week/TableData_Week_County_C.js"

html = requests.get(url)
html.encoding = 'utf8'
page = html.text

# '10017':[
patn = r"\'(\d+)\'\:\["
cityNo = re.findall(patn, page)

date = "2021/12/27"
# 'date':'2021/12/26','time':'12:00','Temp':{'C':{'L':'13','H':'13'}
# patn=r"\'date\'\:\'"+date+"\'\,\'time\'\:\'12\:00\'\,\'Temp\'\:\{\'C\'\:\{(.+?)\}"
# patn=r"\'date\'\:\'"+date+"\'\,\'time\'\:\'\d+\:\d+\'\,\'Temp\'\:\{\'C\'\:\{(.+?)\}"
patn = r"\'date\'\:\'"+date+"\W+time.+Temp\W+C\W+L\W+(\d+).*\:\'(\d+)\'\}\,\'F"
print(patn)
temp = re.findall(patn, page)

url = "https://www.cwb.gov.tw/Data/js/info/Info_County.js"
html1 = requests.get(url)
html1.encoding = 'utf8'
page1 = html1.text
patn1 = r"D\W+(\d+)\W+A.*C\W+(\w+)"
cityPair = re.findall(patn1, page1)

cityData = []
for i in range(len(cityNo)):
    cityname = ""
    for j in cityPair:
        if cityNo[i] == j[0]:
            cityname = j[1]
            break
    # 得到cityNo對應的中文城市名稱
    if cityname != "":
        cityData.append({'city': cityname, 'dayOrNignt': '白天',
                        'high': temp[2*i][1], 'low': temp[2*i][0]})

        cityData.append({'city': cityname, 'dayOrNignt': '晚上',
                        'high': temp[2*i+1][1], 'low': temp[2*i+1][0]})
    else:
        print("city no 無法對應中文城市名稱")
