import requests
from bs4 import BeautifulSoup

url=('http://quotes.toscrape.com/')
response=requests.get(url)
print(response)

html=response.text

soup=BeautifulSoup(html, 'html.parser')
print(soup)