from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=site%3Ahttps%3A%2F%2Fcompetition.aihub.or.kr%2F2022'
while True:
    driver.get(url)
    time.sleep(2)