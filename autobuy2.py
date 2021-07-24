from selenium import webdriver
import time 
from time import sleep
import schedule
import datetime

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.use_chromium = True
options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(executable_path=r'C:\Users\0927r\pyasobi\scraping\chromedriver.exe',options=options)

url1 = "https://bananaman-goods.com/login?redirect_uri=/"
url2 = "https://bananaman-goods.com/items/60f3d62703e59424cc982a89"




def Login():
    driver.get(url1)
    mailad = driver.find_element_by_name("email")
    mailad.send_keys("ryota.s0927@icloud.com")
    password = driver.find_element_by_name("password")
    password.send_keys("023ryota")
    login_btn = driver.find_element_by_class_name("login_button")
    login_btn.click()

def Main():
    time.sleep(3)
    driver.get(url2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/main/div[2]/section[1]/div[2]/div[2]/button').click()

schedule.every().day.at("21:29").do(Login)  
schedule.every().day.at("21:29:55").do(Main)  
while True:
  schedule.run_pending()
  time.sleep(0.1)