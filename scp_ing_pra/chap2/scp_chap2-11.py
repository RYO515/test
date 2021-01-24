import requests

image_url = "https://www.ymori.com/books/python2nen/sample1.png"
# imgdata に 取得した url を代入
imgdata = requests.get(image_url)

# filename に url の後ろから1番目を切り離して代入
filename = image_url.split("/")[-1]

# filename を画像が書き込みできる状態で f として開く
with open(filename, mode="wb") as f:
    # imgdataを書き込む
    f.write(imgdata.content)
