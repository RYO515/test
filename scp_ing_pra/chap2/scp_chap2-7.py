import requests
from bs4 import BeautifulSoup

load_url = "https://yahoo.co.jp"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

topics = soup.find(id="tabpanelTopics7")
for element in topics.find_all("h1"):
    print(element.text)
