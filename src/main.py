import os
import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

# Might move this to its own config file
load_dotenv()

URL = os.getenv('URL')

PAYLOAD = {
  'inUserName': os.getenv('USERNAME'),
  'inUserPass': os.getenv('PASSWORD')
}

# selenium
driver = webdriver.Chrome()

driver.get(URL)

driver.implicitly_wait(0.5)

# Main login page
print(driver.current_url)

login_link = driver.find_element(By.PARTIAL_LINK_TEXT, "deferred offer and enrol")
login_link.click()

driver.find_element(By.NAME, 'username').send_keys(os.getenv('USERNAME'))
driver.find_element(By.NAME, 'password').send_keys(os.getenv('PASSWORD'))

login_btn = driver.find_element(By.XPATH, "//span[contains(text(), 'Agree &')]")
login_btn.click()

driver.implicitly_wait(2)

# Main enrolment page
print(driver.current_url)

enrol_btn = driver.find_element(By.NAME, 'bsdsSubmit-update-enrol')
enrol_btn.click()

# Enrolment page
print(driver.current_url)

select_classes_btn = driver.find_element(By.NAME, 'bsdsSubmit-select-classes')
select_classes_btn.click()

# Select classes page
print(driver.current_url)

html = driver.page_source

# soup obj
soup = BeautifulSoup(html, 'html.parser')

def parse_data():
  parsed_status = []
  status_data = soup.find_all('button')

  for data in status_data:
    if len(data.text) > 1:
      parsed_status.append(data.text)

  return parsed_status

# print(soup.prettify())
print(parse_data())

driver.quit()

# URL_9024 = 'https://timetable.unsw.edu.au/2024/COMP9024.html'

# # response object
# res = requests.post(URL, data=PAYLOAD)
# # soup obj
# soup = BeautifulSoup(res.text, 'html.parser')

# def parse_data():
#   parsed_status = []
#   status_data = soup.find_all('font')

#   for data in status_data:
#     if 'Open' in data or 'Full' in data:
#       parsed_status.append(data.text)

#   return parsed_status

# print(soup.prettify())

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