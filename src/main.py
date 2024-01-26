import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium_funcs import login, navigate_enrolment, select_classes
from csv_funcs import read_csv, write_csv, format_csv

# Might move this to its own config file
load_dotenv()

URL = os.getenv('URL')

# selenium
driver = webdriver.Chrome()
driver.get(URL)
driver.implicitly_wait(2)

login(driver)
navigate_enrolment(driver)
classes_list = select_classes(driver)

driver.quit()

# save parsed data into csv to compare previous version with updated version

csv_data = None;

while not csv_data:
  try:
    csv_data = read_csv()  
  except FileNotFoundError:
    write_csv(classes_list)
    
print('csv: ', len(format_csv(read_csv())))
print('class_list: ', len(classes_list))


# NEXT STEPS:
# figure out time intervals (10 mins) to request again
# if there are changes (new differs from previous) then send txt message to notify (test txt msg first)
# figure out how to listen to multiple requests and send txt msg for each timetable
# after all is done, figure out how to run the script 24/7