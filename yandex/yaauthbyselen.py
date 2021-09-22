from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def yandex_auth(login_id, passw):
    driver = webdriver.Chrome('/Users/rup/Downloads/py-homeworks-advanced-master/chromedriver')
    driver.get('https://passport.yandex.ru/auth')
    login = driver.find_element_by_name('login')
    login.send_keys(login_id)
    login.send_keys(Keys.RETURN)
    time.sleep(4)
    password = driver.find_element_by_name('passwd')
    password.send_keys(passw)
    password.send_keys(Keys.RETURN)
    time.sleep(4)
    first_name = driver.find_element_by_class_name('personal-info__first').text
    last_name = driver.find_element_by_class_name('personal-info__last').text
    driver.close()
    driver.quit()
    return first_name, last_name
