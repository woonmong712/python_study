import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('/Users/woonmong/Downloads/chromedriver')

driver = webdriver.Chrome(service=s)
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/costagram/index')
time.sleep(1)

# 1. 로그인 (codeit/datascience)

driver.find_element(By.CSS_SELECTOR,'a.top-nav__login-link').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'input.login-container__login-input').send_keys('codeit')
driver.find_element(By.CSS_SELECTOR,'input.login-container__password-input').send_keys('datascience')
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'input.login-container__login-button').click()
time.sleep(2)

# 2. 끝까지 스크롤
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(0.5)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 3. 각 썸네일 클릭 -> 닫기 버튼
post_list = driver.find_elements(By.CSS_SELECTOR,'div.post-list__post')

print(post_list)
for list in post_list:
    list.click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,'button.close-btn').click()
    time.sleep(1)

# 4. 웹 드라이버 종료
driver.quit()
