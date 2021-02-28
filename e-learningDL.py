from tkinter import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime,date

def main():
    main = Tk()
    main.geometry("330x175")
    icon = PhotoImage(file = 'C:\projects\e-learningDL\images\icon.png')
    main.iconphoto(False, icon)
    main.title("E-learning Completion")

    title_l = LabelFrame(main, text="Articles Report Download", font=('Arial', 12, "bold"), fg="#212121", pady = 5, padx = 5)
    user_l = Label(title_l, text="User ID", font=('Arial', 12, "bold"), fg="#212121", pady = 5)
    user_field = Entry(title_l, width = 30)
    password_l= Label(title_l, text="Password", font=('Arial', 12, "bold"), fg="#212121", pady = 5)
    password_field = Entry(title_l, width = 30, show = "*")
    from_date_l = Label(title_l, text="Start Date", font=('Arial', 12, "bold"), fg="#212121", pady = 5)
    from_date_field = Entry(title_l, width = 30)
    dl_button = Button(title_l, text="Download", pady = 5, command = lambda:validate_fields(user_field.get(), password_field.get(), from_date_field.get()))

    title_l.pack()
    user_l.grid(row = 1, column = 0,)
    user_field.grid(row = 1, column = 1)
    password_l.grid(row = 2, column = 0)
    password_field.grid(row = 2, column = 1)
    from_date_l.grid(row = 3, column = 0)
    from_date_field.grid(row = 3, column = 1)
    dl_button.grid(row = 4, column = 0, columnspan = 2)

    main.mainloop()

#go to the site and login
def login(user,password, driver):
    try:
        driver.get('https://thd.earlyconnect.com/Account/Login.aspx')
    except:
        return "There is a problem loading the login page"

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
    try:
        driver.get('http://thd.earlyconnect.com/Admin/Report/ArticleList.aspx')
    except:
        return "Cannot load the articles page"

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

#validate al fields are filled out
def validate_fields(user, password, from_date):
    if user == "" or password == "" or from_date == "":
        popup = Tk()
        popup.geometry("200x50")
        popup.title("Error!")
        error = Label(popup, text = "All fields are required.", pady = 10)
        error.pack()
        popup.mainloop()
    else:
        download(user, password, from_date)

#download files calling each function
def download(user, password, from_date):
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install()) #use chrome as the browser for webdriver
    except:
        return "Webdriver not working"
    login(user, password, driver)
    time.sleep(1)
    get_articles(from_date, driver)
    time.sleep(1)
    mainlist = driver.find_element_by_xpath('//*[@id="MainContent_ImageButtonExport"]')
    mainlist.click() #  download list of articles
    articles = driver.find_elements_by_class_name("btn_gray15") #  download each articles' file
    for article in articles:
        download_files(article, driver)
    driver.quit()

#initiate program
if __name__ == "__main__":
    main()
