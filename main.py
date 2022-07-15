from selenium import webdriver
import platform
import time

if platform.system() == 'Windows':
    driver = webdriver.Chrome('./chromedriver.exe')
else:
    driver = webdriver.Chrome('./chromedriver')

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")


url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=site%3Ahttps%3A%2F%2Fcompetition.aihub.or.kr%2F2022'
url_main = 'https://competition.aihub.or.kr/2022'


while True:
    driver.get(url)
    time.sleep(2)
    driver.get(url_main)
    time.sleep(2)