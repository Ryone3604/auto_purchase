from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.use_chromium = True
options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(executable_path=r'C:\Users\0927r\pyasobi\scraping\chromedriver.exe',options=options)
driver.get("https://bananaman-goods.com/login?redirect_uri=/")
mailad = driver.find_element_by_name("email")
mailad.send_keys("ryota.s0927@icloud.com")
password = driver.find_element_by_name("password")
password.send_keys("023ryota")
login_btn = driver.find_element_by_class_name("login_button")
login_btn.click()
time.sleep(2)   #ページ遷移を待つ　すぐだとエラーが出る
cap = driver.find_element_by_class_name("c-itemList__item-link")
cap.click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div/div/main/div[2]/section[1]/div[2]/div[2]/button').click()

