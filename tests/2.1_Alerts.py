from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
sleep(1)
driver.get("https://demoqa.com/alerts")
sleep(5)
#1  alertButton
def alertButton():
    bntAlertButton = driver.find_element(By.ID, 'alertButton')
    bntAlertButton.click()
    sleep(5)
    driver.switch_to.alert.accept()
    sleep(7)
#2   timerAlertButton:
def timerAlertButton():
    bntTimerAlertButton = driver.find_element(By.ID, 'timerAlertButton')
    bntTimerAlertButton.click()
    sleep(10)
    driver.switch_to.alert.accept()
    sleep(5)
#3  confirmButton:  switch_to.alert.accept() & switch_to.alert.dismiss()
def ConfirmButton_OK():
    bntConfirmButton = driver.find_element(By.ID, 'confirmButton')
    bntConfirmButton.click()
    sleep(5)
    driver.switch_to.alert.accept()
    sleep(5)
def ConfirmButton_Cancle():
    bntConfirmButton = driver.find_element(By.ID, 'confirmButton')
    bntConfirmButton.click()
    sleep(5)
    driver.switch_to.alert.dismiss()
    sleep(5)
    
#4 promtButton: switch_to.alert.send_keys('')
def promtButton_OK():
    bntPromtButton = driver.find_element(By.ID, 'promtButton')
    bntPromtButton.click()
    sleep(5)
    driver.switch_to.alert.send_keys('Phạm Thị Thanh Hoa')
    sleep(6)
    driver.switch_to.alert.accept()
    sleep(5)
def promtButton_Cancle():
    bntPromtButton = driver.find_element(By.ID, 'promtButton')
    bntPromtButton.click()
    driver.switch_to.alert.dismiss()
    sleep(5)

alertButton()  
timerAlertButton()
ConfirmButton_OK()
ConfirmButton_Cancle()  
promtButton_OK()
promtButton_Cancle()


