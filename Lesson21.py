def registration():
    from selenium import webdriver
    from helpers.data import user as user_data
    from helpers.waiters import parts
    from helpers.xpath import dumskaya as x

    driver = webdriver.Chrome()
    driver.set_window_position(2000, 600)
    driver.maximize_window()
    url = 'https://dumskaya.net/'
    driver.get(url)
    parts.base_button(driver, x.Home.enter_button)
    parts.base_button(driver, x.Home.registration_button)
    parts.base_field(driver, x.Registration.email_field, user_data.email)
    parts.base_field(driver, x.Registration.nick_field, user_data.nick)
    parts.base_field(driver, x.Registration.password_field, user_data.password)
    parts.base_field(driver, x.Registration.password2_field, user_data.password)
    parts.base_button(driver, x.Registration.male_radio)
    parts.base_button(driver, x.Registration.finish_button)
    return parts.base_label(driver,x.User.user_name_label)