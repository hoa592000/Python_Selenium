from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
sleep(1)
driver.get("https://demoqa.com/browser-windows")
sleep(3)

#New Tab
def newTab():
    btnwindowButton = driver.find_element(By.ID, 'tabButton')
    btnwindowButton.click()
    sleep(5)
    driver.switchTo().defaultContent();
    sleep(2)
    # driver.execute_script("window.open('about:blank', 'secondtab');")
    # driver.switch_to.window("secondtab")
    text1 = driver.find_element(By.ID, 'sampleHeading')
    print(text1)   
# windowButton: current_window_handle & window_handles 
def windowButton():
    btnwindowButton = driver.find_element(By.ID, 'windowButton')
    btnwindowButton.click()
    sleep(5)

    print(driver.current_window_handle)
    #returns all the handle values of opened browse windows
    handles = []
    handles = driver.window_handles 
    for handle in handles:
        print(handle)
        
    #trỏ sang new window    
    newHandle = handles[1]
    driver.switch_to.window(newHandle)
    driver.maximize_window()
    sleep(5)
    textFile = driver.find_element(By.ID, 'sampleHeading')
    print(textFile.text)

# messageWindowButton
def windowMessage():
    btnwindowButton = driver.find_element(By.ID, 'messageWindowButton')
    btnwindowButton.click()
    sleep(5)

    print(driver.current_window_handle)
    #returns all the handle values of opened browse windows
    handle1s = []
    handle1s = driver.window_handles 
    for handle1 in handle1s:
        print(handle1)       
    newHandle1 = handle1s[1]
    driver.switch_to.window(newHandle1)
    driver.maximize_window()
    sleep(5)
    textFile = driver.find_element(By.ID, 'sampleHeading')
    print(textFile.text)
   
windowButton()
windowMessage()
newTab()
