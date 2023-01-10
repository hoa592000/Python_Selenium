from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

def handle1():
    driver.get("https://smart-ocr.egs-dev.site/createform/loginl")
    driver.find_element(By.ID, "input-formatter").send_keys("ifordio")
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    
    action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
    action.send_keys(Keys.TAB).perform()
    action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    action.key_down(Keys.ENTER).perform()
def handle2():
    driver.get("https://m3.material.io/styles/color/the-color-system/key-colors-tones")
    action1 = ActionChains(driver)
    driver.find_element(By.CSS_SELECTOR, "#main_content > nav > div > div > a.tab.ng-tns-c43-1.ng-star-inserted.active > span").click()
    action1.key_down(Keys.ARROW_DOWN).perform()
    action1.key_down(Keys.ARROW_DOWN).perform()
    sleep(2)
    action1.key_down(Keys.ARROW_DOWN).perform()
    sleep(2)
    action1.key_down(Keys.ARROW_DOWN).perform()
    sleep(2)
    action1.key_down(Keys.ARROW_DOWN).perform()
    action1.key_down(Keys.ARROW_UP).perform()
handle1()
# handle2()