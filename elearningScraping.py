from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime,date
from re import *


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://thd.earlyconnect.com/Account/Login.aspx')

time.sleep(1)
user_id = driver.find_element_by_xpath('//*[@id="TextBoxUserId"]')
pswd = driver.find_element_by_xpath('//*[@id="TextBoxPasswd"]')
login_btn = driver.find_element_by_xpath('//*[@id="login"]')

user_id.send_keys('jose.cornielhiciano@alorica.com')
pswd.send_keys('sjwVbXX6')
login_btn.click()

time.sleep(1)

driver.get('http://thd.earlyconnect.com/Admin/Report/ArticleList.aspx')

global from_date
from_date = "11-17-2020"

from_date_field = driver.find_element_by_xpath('//*[@id="MainContent_TextBoxFromDate"]')
tips = driver.find_element_by_xpath('//*[@id="MainContent_CheckBoxTip"]')
refresh = driver.find_element_by_xpath('//*[@id="container"]/div[3]/div[1]/table/tbody/tr[1]/td[3]/a')
from_date_field.send_keys(from_date)
tips.click()
refresh.click()
time.sleep(1)
articles = driver.find_elements_by_class_name("btn_gray15")

def download_files():
    details = article.get_attribute('href')
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(details)
    time.sleep(1)
    file = driver.find_element_by_name('ctl00$MainContent$ImageButtonExport')
    file.click()
    driver.switch_to.window(driver.window_handles[0])


for article in articles:
    download_files()
