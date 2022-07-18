from selenium import webdriver
import platform
import time

if platform.system() == 'Windows':
    driver = webdriver.Chrome('./chromedriver.exe')
else:
    driver = webdriver.Chrome('./chromedriver')

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")


url1 = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=site%3Ahttps%3A%2F%2Fcompetition.aihub.or.kr%2F2022'
url2 = 'https://search.naver.com/search.naver?where=nexearch&sm=top_sly.hst&fbm=1&acr=1&ie=utf8&query=%ED%95%9C%EA%B5%AD%EC%96%B4+AI+%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C'
url3 = 'https://competition.aihub.or.kr/2022'
url4 = 'https://search.naver.com/search.naver?where=nexearch&sm=top_sly.hst&fbm=1&acr=2&ie=utf8&query=2022+%ED%95%9C%EA%B5%AD%EC%96%B4+AI+%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C'
url5 = 'https://competition.aihub.or.kr/2022'

while True:
    driver.get(url1)
    time.sleep(2)
    driver.get(url2)
    time.sleep(2)
    driver.get(url3)
    time.sleep(2)
    driver.get(url4)
    time.sleep(2)
    driver.get(url5)
    time.sleep(2)