import requests

url = "https://www.ymori.com/books/python2nen/test1.html"
response = requests.get(url)

# 日本語が文字化けしないようにする
response.encoding = response.apparent_encoding

filename = "download.txt"
# fileを書き込みモードで開く
f = open(filename, mode="w")
# インターネットから取得したデータを書き込む
f.write(response.text)

# ファイルを閉じる
f.close()
