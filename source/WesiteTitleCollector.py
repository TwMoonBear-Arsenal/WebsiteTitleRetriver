# 從標準庫引用
import urllib.request

# 匯入Pypi的BeautifulSoup4 package
from bs4 import BeautifulSoup

# 開啟網頁
response = urllib.request.urlopen('http://www.google.com/')

# 解析網頁
soup = BeautifulSoup(response, features="html.parser")

# 列印網頁標題
print(soup.title.string)
