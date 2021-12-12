import requests

url = 'https://store.steampowered.com'
data = requests.get(url)

if data.status_code != 200:
    print("請求失敗{}: url={} " . format(data.status_code, url))
else:
    print("請求成功")
