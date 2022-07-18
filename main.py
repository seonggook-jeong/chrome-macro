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
url2 = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%95%9C%EA%B5%AD%EC%96%B4+AI+%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C&oquery=%ED%95%9C%EA%B5%AD%EC%96%B4+AI+%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C&tqi=hWfy%2BwprvTVssg2zM7NssssssQC-114492'
url3 = 'https://competition.aihub.or.kr/2022'


while True:
    driver.get(url1)
    time.sleep(2)
    driver.get(url2)
    time.sleep(2)
    driver.get(url3)
    time.sleep(2)