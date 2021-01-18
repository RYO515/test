import requests

url = "https://www.ymori.com/books/python2nen/test1.html"
# getしたurlをリクエストしてresponseにいれる
response = requests.get(url)

# 文字化けをしないようにする
response.encoding = response.apparent_encoding

print(response.text)
