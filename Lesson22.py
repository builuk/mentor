#https://refactoring.guru/uk/design-patterns
#https://selenium-python.readthedocs.io/page-objects.html

'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def init(self, driver):
        self.driver = driver

class LoginPage(BasePage):
    def init(self, driver):
        super().init(driver)
        self.username_input = (By.ID, 'username')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'login-btn')

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

class HomePage(BasePage):
    def init(self, driver):
        super().init(driver)
        self.welcome_message = (By.ID, 'welcome-msg')
        self.logout_button = (By.ID, 'logout-btn')

    def get_welcome_message(self):
        return self.driver.find_element(*self.welcome_message).text

    def logout(self):
        self.driver.find_element(*self.logout_button).click()

# Пример использования в тестах
driver = webdriver.Chrome()
driver.get("http://yourwebsite.com")

login_page = LoginPage(driver)
login_page.login("your_username", "your_password")

home_page = HomePage(driver)
welcome_msg = home_page.get_welcome_message()
print(welcome_msg)  # Выводит приветственное сообщение после успешной авторизации

home_page.logout()
driver.quit()'''


from selenium import webdriver
from pages import base
import helpers.data.user as user_data
import time
# Або так, або так
# from pages.base import HomePage as h
# from pages.base import RegistrationPage as r

driver = webdriver.Chrome()
driver.set_window_position(2000, 600)
driver.maximize_window()
url = 'https://dumskaya.net/'
driver.get(url)
home = base.HomePage(driver)
reg = base.RegistrationPage(driver)
top = base.TopPage(driver)
# home.open_articles_page()

# Розібратись чого не працює
# home.open_home_page()
home.user_menu()
home.registration_user()
# reg.registration(user_data.email,user_data.nick,user_data.password)
home.open_top_page()
print(top.first_line())
