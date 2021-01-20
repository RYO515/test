import requests
from pathlib import Path

out_folder = Path("download")
# folder の作成
out_folder.mkdir(exist_ok=True)

image_url = "https://www.ymori.com/books/python2nen/sample1.png"
imagedata = requests.get(image_url)

filename = image_url.split("/")[-1]
out_path = out_folder.joinpath(filename)

with open(out_path, mode="wb") as f:
    f.write(imagedata.content)
