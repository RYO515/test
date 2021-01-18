from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

# アクセスしたいページのURL
driver.get("http://www.python.org")
assert "Python" in driver.title
# 検索ボックスを探す
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
# 検索
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
print(driver.page_source)
driver.close()