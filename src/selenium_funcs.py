import os
from selenium.webdriver.common.by import By

def login(driver):
  # Main login page
  print(driver.current_url)

  login_link = driver.find_element(By.PARTIAL_LINK_TEXT, "deferred offer and enrol")
  login_link.click()

  driver.find_element(By.NAME, 'username').send_keys(os.getenv('USERNAME'))
  driver.find_element(By.NAME, 'password').send_keys(os.getenv('PASSWORD'))

  login_btn = driver.find_element(By.XPATH, "//span[contains(text(), 'Agree &')]")
  login_btn.click()

  driver.implicitly_wait(2)

def navigate_enrolment(driver):
  # Main enrolment page
  print(driver.current_url)

  enrol_btn = driver.find_element(By.NAME, 'bsdsSubmit-update-enrol')
  enrol_btn.click()

  # Enrolment page
  print(driver.current_url)

  select_classes_btn = driver.find_element(By.NAME, 'bsdsSubmit-select-classes')
  select_classes_btn.click()

def select_classes(driver):
  # Select classes page
  print(driver.current_url)

  driver.implicitly_wait(2)

  li_classes = driver.find_elements(By.XPATH, "//li[@style='display: flex; width: 100%;']")

  classes = []

  for li_class in li_classes:
    classes.append(li_class.find_element(By.TAG_NAME, 'button').text)
    # classes.append(li_class.find_element(By.TAG_NAME, 'span'))

  filtered_classes = [class_slot for class_slot in classes if len(class_slot) > 1]
  print(filtered_classes)