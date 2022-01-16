import requests
import re
import json
from bs4 import BeautifulSoup

keyword = '數據工程師'
now_page = 1
total_page = 1
result_dict = []

while now_page <= total_page:
    url = 'https://www.1111.com.tw/search/job?ks={}&page={}&act=load_page' \
        .format(keyword, now_page)
    html = json.loads(requests.get(url).text)['html']
    soup = BeautifulSoup(html, 'lxml')
    for sub in soup.select('.item__job'):
        job = {}
        job['name'] = sub.select_one('.item__job-position0--link').get('title')

        company_info = sub.select_one('.item__job-organ--link')
        job['link'] = company_info.get('href')
        job['company'] = re.findall(
            r"《公司名稱》(.+)", company_info.get('title'))[0]

        job['salary'] = sub.select_one(
            '.item__job-prop-salary').get('aria-label')

        result_dict.append(job)
    now_page += 1
