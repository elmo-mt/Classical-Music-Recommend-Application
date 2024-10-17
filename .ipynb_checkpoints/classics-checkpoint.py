import requests
from bs4 import BeautifulSoup

# urlのサイトの情報をもらってくる
url = "https://www.universal-music.co.jp/classics/classic-dept-commentary/cat/concerto/"
response = requests.get(url)

response.text[:500]
