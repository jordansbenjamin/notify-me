import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium_funcs import login, navigate_enrolment, select_classes

# Might move this to its own config file
load_dotenv()

URL = os.getenv('URL')

# selenium
driver = webdriver.Chrome()
driver.get(URL)
driver.implicitly_wait(2)

login(driver)
navigate_enrolment(driver)
select_classes(driver)

driver.quit()

# save parsed data into csv to compare previous version with updated version

# csv_data = None;

# try:
#   with open('status_data.csv') as status_csvf:
#     # reader = csv.reader(status_csvf)
#     # csv_data.append(reader)
#     csv_data = status_csvf.readlines()
# except:
#   with open('status_data.csv', 'w') as status_csvf:
#     writer = csv.writer(status_csvf)
#     writer.writerow(parse_data())

# new_csv_data = None

# try:
#   with open('new_status_data.csv') as status_csvf:
#     # reader = csv.reader(status_csvf)
#     # csv_data.append(reader)
#     new_csv_data = status_csvf.readlines()
# except:
#   with open('new_status_data.csv', 'w') as status_csvf:
#     writer = csv.writer(status_csvf)
#     writer.writerow(parse_data())

# def format_csv(data):
#   if data:
#     formatted_csv_data = data[0].split(',')
#     return formatted_csv_data

# print(len(format_csv(csv_data)))
# print(len(format_csv(new_csv_data)))

# NEXT STEPS:
# figure out time intervals (10 mins) to request again
# if there are changes (new differs from previous) then send txt message to notify (test txt msg first)
# figure out how to listen to multiple requests and send txt msg for each timetable
# after all is done, figure out how to run the script 24/7