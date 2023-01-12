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
#TextBox
#Box = driver.find_elements(By.TAG_NAME, '')
def TextBox():
    textName = driver.find_element(By.ID, 'userName')
    textName.send_keys("Test1")
    textEmail = driver.find_element(By.ID, 'userEmail')
    textEmail.send_keys("Test2@gmail.com")
    textCurrentAddrest = driver.find_element(By.ID, 'currentAddress')
    textCurrentAddrest.send_keys("Test3")
    textPermanetAddres = driver.find_element(By.ID, 'permanentAddress')
    textPermanetAddres.send_keys("Test4")
    btnSubmit = driver.find_element(By.CSS_SELECTOR, 'button[btn.btn-primary][id="submit"]')
    btnSubmit.click()
    # sleep(10)
def CheckBox():
    # li[class="btn btn-light active"][id="item-0"]
    # buttonCheckBox = driver.find_element(By.CSS_SELECTOR, 'li[class="btn btn-light active"][id="item-1"]')
    # buttonCheckBox.click()
    buttonMenu = driver.find_element(By.CSS_SELECTOR, 'svg.rct-icon.rct-icon-expand-close')
    buttonMenu.click()
    buttonDesktop = driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > span > button > svg')
    buttonDesktop.click()
    buttonDocuments = driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li:nth-child(2) > span > button > svg')
    buttonDocuments.click()
    buttonDownloads = driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li:nth-child(3) > span > button > svg')
    buttonDownloads.click()
    
    buttonSelectAll = driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > span > label > span.rct-checkbox > svg')
    buttonSelectAll.click()
    buttonSelectDesktop = driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li:nth-child(1) > span > label > span.rct-checkbox > svg')
    buttonSelectNotes = driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > label > span.rct-checkbox > svg')
    buttonSelectcommands = driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(2) > span > label > span.rct-checkbox > svg')
    buttonSelectDocuments = driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li:nth-child(2) > span > label > span.rct-checkbox > svg')
    buttonSelectDownloads = driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li:nth-child(3) > span > label > span.rct-checkbox > svg')

TextBox()
# CheckBox()