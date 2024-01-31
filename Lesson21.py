from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import xpath_dumskaya as x
import user_data
from helpers.waiters import parts

driver = webdriver.Chrome()
driver.set_window_position(2000, 600)
driver.maximize_window()
url = 'https://dumskaya.net/'
driver.get(url)

parts.base_button(driver, x.enter_button)
parts.base_button(driver, x.registration_button)

parts.base_field(driver, x.email_field, user_data.email)

nick_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.nick_field)))
nick_field.send_keys(user_data.nick)

password_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.password_field)))
password_field.send_keys(user_data.password)

password2_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.password2_field)))
password2_field.send_keys(user_data.password)

male_radio = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.male_radio)))
male_radio.click()

finish_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.finish_button)))
finish_button.click()

time.sleep(3000)