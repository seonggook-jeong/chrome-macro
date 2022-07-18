from selenium import webdriver
import platform
import time

if platform.system() == 'Windows':
    driver = webdriver.Chrome('./chromedriver.exe')
else:
    driver = webdriver.Chrome('./chromedriver')

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")



urls = list(map(lambda x: x.replace('\n',''), open('urls.txt',encoding='utf-8').readlines()))

while True:
    for url in urls:
        driver.get(url)
        if driver.current_url=='http://cr.naver.com/redirect-notification?u=https%3A%2F%2Fcompetition.aihub.or.kr%2F2022':
            time.sleep(.4)
            driver.get('https://competition.aihub.or.kr/2022')
        time.sleep(3)