from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime,date

#Set chrome as driver app
driver = webdriver.Chrome(ChromeDriverManager().install())

#go to the site and login
def login(user,pwd):
    driver.get('https://thd.earlyconnect.com/Account/Login.aspx')

    #select elements to pass arguments
    user_id = driver.find_element_by_xpath('//*[@id="TextBoxUserId"]')
    pswd = driver.find_element_by_xpath('//*[@id="TextBoxPasswd"]')
    login_btn = driver.find_element_by_xpath('//*[@id="login"]')

    #passing arguments
    user_id.send_keys(user)
    pswd.send_keys(pwd)
    login_btn.click()

#go the the articles list page and list all articles
def get_articles(from_date):
    driver.get('http://thd.earlyconnect.com/Admin/Report/ArticleList.aspx')

    #select elements to pass arguments
    from_date_field = driver.find_element_by_xpath('//*[@id="MainContent_TextBoxFromDate"]')
    tips = driver.find_element_by_xpath('//*[@id="MainContent_CheckBoxTip"]')
    refresh = driver.find_element_by_xpath('//*[@id="container"]/div[3]/div[1]/table/tbody/tr[1]/td[3]/a')

    #passing arguments
    from_date_field.send_keys(from_date)
    tips.click()
    refresh.click()

#download articles details file
def download_files():
    details = article.get_attribute('href') #get the link to the details of each article
    driver.execute_script("window.open('');") #javascript to open details page
    driver.switch_to.window(driver.window_handles[1]) #switch to details tab
    driver.get(details) #go to the details page of the article
    time.sleep(1) #wait for page to load
    file = driver.find_element_by_name('ctl00$MainContent$ImageButtonExport') #select export button
    file.click() #press the export button
    driver.switch_to.window(driver.window_handles[0]) #switch to the original tab to open next articles details

login()

time.sleep(1)

get_articles()

time.sleep(1)

articles = driver.find_elements_by_class_name("btn_gray15")

for article in articles:
    download_files()
