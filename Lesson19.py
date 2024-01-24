from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.set_window_position(2000, 600)

driver.maximize_window()

url = "https://test.mensa.no/"

driver.get(url)

age1850_xpath = '//button[contains(@class,"ageselect_1850")]'
age1850_button = driver.find_element(By.XPATH, age1850_xpath)
age1850_button.click()
time.sleep(3)

start_id = 'startTest'
start_button = driver.find_element(By.ID, start_id)
start_button.click()
time.sleep(3)

q1_a_xpath = '//div[@id="question_0"]//div[@data-answerid="0"]'
q1_a_button = driver.find_element(By.XPATH, q1_a_xpath)
q1_a_button.click()
time.sleep(3)

q2_a_xpath = '//div[@id="question_1"]//div[@data-answerid="1"]'
q2_a_button = driver.find_element(By.XPATH, q2_a_xpath)
q2_a_button.click()
time.sleep(3)


time.sleep(3000)