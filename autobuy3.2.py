from selenium import webdriver
import time 
from time import sleep
import schedule
from datetime import timedelta
import datetime
import requests
from bs4 import BeautifulSoup
import time
import math

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.use_chromium = True
options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(executable_path=r'C:\Users\0927r\pyasobi\scraping\chromedriver.exe',options=options)

url1 = "https://bananaman-goods.com/login?redirect_uri=/"
url2 = "https://bananaman-goods.com/items/60f3d62703e59424cc982a89"

start = "22:41:00"
start1 = datetime.datetime.strptime(start, '%H:%M:%S').time()
start2 = datetime.datetime.combine(datetime.date.today(), start1) - datetime.timedelta(minutes=2)
start3 = start2.strftime("%H:%M:%S")

r = requests.get('https://ntp-a1.nict.go.jp/cgi-bin/jst')
soup = BeautifulSoup(r.text,'lxml')
t1 = soup.find("body").string
t2 = t1.rstrip('\n')
t3 = time.time()
t4 = float(t2)-t3
if t4 >= 0:
    t5 = 0
    t6 = math.ceil(t4)
    t7 = t4 - t6

else:
    t5 = -t4
    t6 = 0
    t7 = 0

start5 = datetime.datetime.combine(datetime.date.today(), start1) + datetime.timedelta(seconds = t6)
start6 = start5.strftime("%H:%M:%S")


def Login():
    driver.get(url1)
    mailad = driver.find_element_by_name("email")
    mailad.send_keys("ryota.s0927@icloud.com")
    password = driver.find_element_by_name("password")
    password.send_keys("023ryota")
    login_btn = driver.find_element_by_class_name("login_button")
    login_btn.click()
    time.sleep(0.5)   #ページ遷移を待つ　すぐだとエラーが出る
    cap = driver.find_element_by_class_name("c-itemList__item-link")
    cap.click()

def Main():
    time.sleep(0.5)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/main/div[2]/section[1]/div[2]/div[2]/button').click()

schedule.every().day.at(start3).do(Login)  
schedule.every().day.at(start6).do(Main)  
while True:
  schedule.run_pending()
  time.sleep(0.1)