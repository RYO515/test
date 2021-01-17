FROM python:3.9

# パッケージの更新確認
RUN apt-get -y update

#chromeブラウザのインストール 
RUN apt-get install -y unzip
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
RUN echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update
RUN apt-get -y install google-chrome-stable

# chromeドライバのインストール 
# RUN curl -OL https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_linux64.zip && unzip chromedriver_linux64.zip chromedriver && mv chromedriver /usr/bin/chromedriver
RUN curl -OL https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip && unzip chromedriver_linux64.zip chromedriver && mv chromedriver /usr/bin/chromedriver

COPY . .

RUN pip install selenium==3.141.0
