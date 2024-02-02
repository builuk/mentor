from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Загрузка драйвера браузера (укажите свой путь к драйверу)
driver = webdriver.Chrome()

# Открыть страницу регистрации
driver.get('https://dumskaya.net/')

# Найти и нажать на кнопку "Зарегистрироваться"
register_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Регистрация')]"))
)
register_button.click()

# Заполнение формы регистрации
email_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "email"))
)
email_input.send_keys("your_email@example.com")

password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("your_password")

# Заполнение остальных полей формы по аналогии

# Нажать на кнопку "Зарегистрироваться"
register_submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
register_submit_button.click()
