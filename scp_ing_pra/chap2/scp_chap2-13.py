import requests
from bs4 import BeautifulSoup
import urllib

load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

for element in soup.find_all("img"):
    src = element.get("src")

    image_url = urllib.parse.urljoin(load_url, src)
    filename = image_url.split("/")[-1]
    print(image_url, ">>", filename)
