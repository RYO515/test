import requests
from bs4 import BeautifulSoup

url_load = "https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(url_load)
soup = BeautifulSoup(html.content, "html.parser")

print(soup)