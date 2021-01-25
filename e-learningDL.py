from tkinter import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime,date

def main():
    main = Tk()
    main.geometry("300x200")

    title_l = Label(main, text="E-learning Articles Download", font=('Arial', 12, "bold"), fg="#212121")
    user_l = Label(main, text="User ID", font=('Arial', 12, "bold"), fg="#212121")
    user_field = Entry(main)
    password_l= Label(main, text="Password", font=('Arial', 12, "bold"), fg="#212121")
    password_field = Entry(main, show = "*")
    from_date_l = Label(main, text="From Date", font=('Arial', 12, "bold"), fg="#212121")
    from_date_field = Entry(main)
    dl_button = Button(main, text="Download", command = lambda:validate_fields(user_field.get(), password_field.get(), from_date_field.get()))

    title_l.grid(row = 0, column = 0, columnspan = 2)
    user_l.grid(row = 2, column = 0)
    user_field.grid(row = 2, column = 1)
    password_l.grid(row = 3, column = 0)
    password_field.grid(row = 3, column = 1)
    from_date_l.grid(row = 4, column = 0)
    from_date_field.grid(row = 4, column = 1)
    dl_button.grid(row = 5, column = 0, columnspan = 2)

    main.mainloop()

#go to the site and login
def login(user,password, driver):
    driver.get('https://thd.earlyconnect.com/Account/Login.aspx')

    #select elements to pass arguments
    user_id = driver.find_element_by_xpath('//*[@id="TextBoxUserId"]')
    pswd = driver.find_element_by_xpath('//*[@id="TextBoxPasswd"]')
    login_btn = driver.find_element_by_xpath('//*[@id="login"]')

    #passing arguments
    user_id.send_keys(user)
    pswd.send_keys(password)
    login_btn.click()

#go the the articles list page and list all articles
def get_articles(from_date, driver):
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
def download_files(article, driver):
    details = article.get_attribute('href') #get the link to the details of each article
    driver.execute_script("window.open('');") #javascript to open details page
    driver.switch_to.window(driver.window_handles[1]) #switch to details tab
    driver.get(details) #go to the details page of the article
    time.sleep(1) #wait for page to load
    file = driver.find_element_by_name('ctl00$MainContent$ImageButtonExport') #select export button
    file.click() #press the export button
    driver.switch_to.window(driver.window_handles[0]) #switch to the original tab to open next articles details

def validate_fields(user, password, from_date):
    if user == "" or password == "" or from_date == "":
        popup = Tk()
        error = Label(popup, text = "All fields are required.")
        error.pack()
    else:
        download(user, password, from_date)

def download(user, password, from_date):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    login(user, password, driver)
    time.sleep(1)
    get_articles(from_date, driver)
    time.sleep(1)
    articles = driver.find_elements_by_class_name("btn_gray15")
    for article in articles:
        download_files(article, driver)

if __name__ == "__main__":
    main()
