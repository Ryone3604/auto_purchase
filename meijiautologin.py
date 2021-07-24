from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\0927r\pyasobi\scraping\chromedriver.exe')
driver.get("https://oh-o2.meiji.ac.jp/portal/index")
driver.find_element_by_xpath('//*[@id="loginField"]/dl/dt/a').click() #id,classがないからxpathで
accountid = driver.find_element_by_name("ACCOUNTUID")
accountid.send_keys("1810190398")
password = driver.find_element_by_name("PASSWORD")
password.send_keys("023ryotaS")
signin_btn = driver.find_element_by_name("SUBMIT")
signin_btn.click()