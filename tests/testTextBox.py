from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
# driver = webdriver.Chrome(PATH, chrome_options= chrome_option)
sleep(1)
driver.get("https://demoqa.com/text-box")
sleep(5)
# Elements
    # Box = driver.find_elements(By.TAG_NAME, '')
#TextBox
# def Elements():
textName = driver.find_element(By.ID, 'userName')
textName.send_keys("Test1")
sleep(5)
textEmail = driver.find_element(By.ID, 'userEmail')
textEmail.send_keys("Test2")
sleep(5)
textCurrentAddrest = driver.find_element(By.ID, 'currentAddress')
textCurrentAddrest.send_keys("Test3")
sleep(5)
textPermanetAddres = driver.find_element(By.ID, 'permanentAddress')
textPermanetAddres.send_keys("Test4")
sleep(5)
btnSubmit = driver.find_element(By.ID, 'submit')
btnSubmit.click()
sleep(10)

# Elements()
#CheckBox

#Forms
#Alerts, Frame & Windowns
#Widgets
#Interations
#Book Store Application