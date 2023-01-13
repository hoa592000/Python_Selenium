from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
sleep(1)
driver.get("https://demoqa.com/automation-practice-form")
sleep(5)

def element():
    textFirstName = driver.find_element()
    textLastName = driver.find_element()
    textEmail = driver.find_element()
    textGender = driver.find_element()



# import openpyxl as O
# Execl_file = "Book1.xlsx"
# Excel_worksheet= "Sheet1"
# wb = O.load_workbook(Execl_file)
# ws = wb[Excel_worksheet]
# row_num = ws.max_row
# col_num = ws.max_column
# print("Row is ", row_num, "Colume", col_num)
# row = 1
# print("Value is ",ws.cell(row,3).value)
