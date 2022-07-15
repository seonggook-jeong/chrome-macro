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
url_main = 'https://search.naver.com/p/crd/rd?m=1&px=1136&py=2068&sx=1136&sy=419&p=hWZAjdprvh8ssBhnpklssssssvZ-358150&q=2022+%ED%95%9C%EA%B5%AD%EC%96%B4+AI+%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C&ie=utf8&rev=1&ssc=tab.web.all&f=web&w=web&s=mNgHMgHL6vUOc6xi5IIWQ17I&time=1657873006801&a=web_lis*w.link&r=11&i=a00000fa_5723278b98852b5f66d920e5&u=https%3A%2F%2Fcompetition.aihub.or.kr%2F2022'


while True:
    driver.get(url)
    time.sleep(2)
    driver.get(url_main)
    time.sleep(2)