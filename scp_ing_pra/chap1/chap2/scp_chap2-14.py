import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time

load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# 保存用のフォルダーを作る
out_folder = Path("download2")
# exist_ok=True 末端ディレクトリが存在している場合もエラーが発生しない
out_folder.mkdir(exist_ok=True)

# 全ての img タグを検索して element にリンクを入れる
for element in soup.find_all("img"):
    src = element.get("src")
    
    # 絶対URLを作って画像データを取得する
    image_url = urllib.parse.urljoin(load_url, src)
    imgdata = requests.get(image_url)
    
    # URLから最後のファイル名を取り出して、保存フォルダ名とつなげる
    filename = image_url.split("/")[-1]
    out_path = out_folder.joinpath(filename)

    with open(filename, mode="wb") as f:
        f.write(imgdata.content)

    time.sleep(1)
