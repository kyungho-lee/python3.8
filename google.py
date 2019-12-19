from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #마지막 K는 capital letter
# import bs4
# soup = bs4.BeautifulSoup()
# from bs4 import BeautifulSoup
# soup = BeautifulSoup()

path ='./chromedriver.exe'  # 현재위치에서 해당 드라이버를 가져오겠다.
driver = webdriver.Chrome(path)
driver.get('https://www.google.com/')

search_input = driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
search_input.send_keys('코리아보드게임')
search_input.send_keys(Keys.RETURN)

# #tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input :구글입력창 위치
