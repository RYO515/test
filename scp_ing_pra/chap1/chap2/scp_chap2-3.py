import requests
from bs4 import BeautifulSoup

url_load = "https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(url_load)
suop = BeautifulSoup(html.content, "html.parser")

print(suop.find("title").text)
print(suop.find("h2").text)
print(suop.find("li").text)
