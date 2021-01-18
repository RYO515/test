import requests

url = "https://www.ymori.com/books/python2nen/test1.html"
response = requests.get(url)

# 日本語が文字化けしないようにする
response.encoding = response.apparent_encoding

filename = "download.txt"
# with文で書くとopenとクローズがセットでcloseを書く必要ない
with open(filename, mode="w") as f:
    f.write(response.text)
