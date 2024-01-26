import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from csv_funcs import write_csv
from data import check_data
from send_sms import send_sms

def login(driver):
  # Main login page
  # print(driver.current_url)

  login_link = driver.find_element(By.PARTIAL_LINK_TEXT, "deferred offer and enrol")
  login_link.click()

  driver.find_element(By.NAME, 'username').send_keys(os.getenv('USERNAME'))
  driver.find_element(By.NAME, 'password').send_keys(os.getenv('PASSWORD'))

  login_btn = driver.find_element(By.XPATH, "//span[contains(text(), 'Agree &')]")
  login_btn.click()

  driver.implicitly_wait(2)

def navigate_enrolment(driver):
  # Program enrolment page
  # print(driver.current_url)

  enrol_btn = driver.find_element(By.NAME, 'bsdsSubmit-update-enrol')
  enrol_btn.click()

  # Courses enrolment page
  # print(driver.current_url)

  select_classes_btn = driver.find_element(By.NAME, 'bsdsSubmit-select-classes')
  select_classes_btn.click()

def select_classes(driver):
  # Select classes page
  # print(driver.current_url)

  driver.implicitly_wait(2)

  li_classes = driver.find_elements(By.XPATH, "//li[@style='display: flex; width: 100%;']")

  classes = []

  for li_class in li_classes:
    classes.append(li_class.find_element(By.TAG_NAME, 'button').text)
    # classes.append(li_class.find_element(By.TAG_NAME, 'span'))

  filtered_classes = [class_slot for class_slot in classes if len(class_slot) > 1]
  # print(filtered_classes)
  
  return filtered_classes

def main_selenium_process(URL):
  driver = webdriver.Chrome()
  driver.get(URL)
  driver.implicitly_wait(2)

  login(driver)
  navigate_enrolment(driver)
  classes_list = select_classes(driver)

  driver.quit()

  if os.path.exists('status_data.csv'):
    write_csv(classes_list, 'new_status_data.csv')
    # check if previous data differs from new data
    if check_data():
      # if it differs, then send the txt msg
      send_sms("There's a new slot for class timetables, check it now!")
      # reset status_data_csv
      write_csv(classes_list, 'status_data.csv')
  else:
    write_csv(classes_list, 'status_data.csv')

  return classes_list