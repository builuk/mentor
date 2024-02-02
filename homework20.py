from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from helpers.xpath import mensa as x

driver = webdriver.Chrome()
driver.set_window_position(2000, 600)
driver.maximize_window()
url = "https://test.mensa.no"
driver.get(url)

age1850_xpath_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.age1850_xpath)))
age1850_xpath_button.click()

start_id_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, x.start_id)))
start_id_button.click()

ex1_a_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex1_a_xpath)))
ActionChains(driver).move_to_element(ex1_a_button).click(ex1_a_button).perform()

ex2_b_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex2_b_xpath)))
ActionChains(driver).move_to_element(ex2_b_button).click(ex2_b_button).perform()

ex3_c_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex3_c_xpath)))
ActionChains(driver).move_to_element(ex3_c_button).click(ex3_c_button).perform()

ex4_d_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex4_d_xpath)))
ActionChains(driver).move_to_element(ex4_d_button).click(ex4_d_button).perform()

ex5_e_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex5_e_xpath)))
ActionChains(driver).move_to_element(ex5_e_button).click(ex5_e_button).perform()

ex6_f_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex6_f_xpath)))
ActionChains(driver).move_to_element(ex6_f_button).click(ex6_f_button).perform()

ex7_a_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex7_a_xpath)))
ActionChains(driver).move_to_element(ex7_a_button).click(ex7_a_button).perform()

ex8_b_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex8_b_xpath)))
ActionChains(driver).move_to_element(ex8_b_button).click(ex8_b_button).perform()

ex9_c_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex9_c_xpath)))
ActionChains(driver).move_to_element(ex9_c_button).click(ex9_c_button).perform()

ex10_d_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex10_d_xpath)))
ActionChains(driver).move_to_element(ex10_d_button).click(ex10_d_button).perform()

ex11_e_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex11_e_xpath)))
ActionChains(driver).move_to_element(ex11_e_button).click(ex11_e_button).perform()

ex12_f_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex12_f_xpath)))
ActionChains(driver).move_to_element(ex12_f_button).click(ex12_f_button).perform()

ex13_a_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex13_a_xpath)))
ActionChains(driver).move_to_element(ex13_a_button).click(ex13_a_button).perform()

ex14_b_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex14_b_xpath)))
ActionChains(driver).move_to_element(ex14_b_button).click(ex14_b_button).perform()

ex15_c_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex15_c_xpath)))
ActionChains(driver).move_to_element(ex15_c_button).click(ex15_c_button).perform()

ex16_d_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex16_d_xpath)))
ActionChains(driver).move_to_element(ex16_d_button).click(ex16_d_button).perform()

ex17_e_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex17_e_xpath)))
ActionChains(driver).move_to_element(ex17_e_button).click(ex17_e_button).perform()

time.sleep(3)
ex18_f_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex18_f_xpath)))
ActionChains(driver).move_to_element(ex18_f_button).click(ex18_f_button).perform()
time.sleep(3)
ex19_a_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex19_a_xpath)))
ActionChains(driver).move_to_element(ex19_a_button).click(ex19_a_button).perform()

ex20_b_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex20_b_xpath)))
ActionChains(driver).move_to_element(ex20_b_button).click(ex20_b_button).perform()

ex21_c_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex21_c_xpath)))
ActionChains(driver).move_to_element(ex21_c_button).click(ex21_c_button).perform()

ex22_d_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex22_d_xpath)))
ActionChains(driver).move_to_element(ex22_d_button).click(ex22_d_button).perform()

ex23_e_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex23_e_xpath)))
ActionChains(driver).move_to_element(ex23_e_button).click(ex23_e_button).perform()

ex24_f_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex24_f_xpath)))
ActionChains(driver).move_to_element(ex24_f_button).click(ex24_f_button).perform()

ex25_a_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex25_a_xpath)))
ActionChains(driver).move_to_element(ex25_a_button).click(ex25_a_button).perform()
time.sleep(3)
ex26_b_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex26_b_xpath)))
ActionChains(driver).move_to_element(ex26_b_button).click(ex26_b_button).perform()
time.sleep(3)
ex27_c_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex27_c_xpath)))
ActionChains(driver).move_to_element(ex27_c_button).click(ex27_c_button).perform()

ex28_d_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex28_d_xpath)))
ActionChains(driver).move_to_element(ex28_d_button).click(ex28_d_button).perform()

ex29_e_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex29_e_xpath)))
ActionChains(driver).move_to_element(ex29_e_button).click(ex29_e_button).perform()

ex30_f_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex30_f_xpath)))
ActionChains(driver).move_to_element(ex30_f_button).click(ex30_f_button).perform()

ex31_a_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex31_a_xpath)))
ActionChains(driver).move_to_element(ex31_a_button).click(ex31_a_button).perform()

ex32_b_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex32_b_xpath)))
ActionChains(driver).move_to_element(ex32_b_button).click(ex32_b_button).perform()

ex33_c_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex33_c_xpath)))
ActionChains(driver).move_to_element(ex33_c_button).click(ex33_c_button).perform()

ex34_d_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex34_d_xpath)))
ActionChains(driver).move_to_element(ex34_d_button).click(ex34_d_button).perform()

ex35_e_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.ex35_e_xpath)))
ActionChains(driver).move_to_element(ex35_e_button).click(ex35_e_button).perform()

finish_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.finish_xpath)))
finish_button.click()

done_already_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.done_already_xpath)))
done_already_button.click()

time.sleep(300)