from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.NAME, "first_name")
    firstname.send_keys("Stanislav")
    lastname = browser.find_element(By.NAME, "last_name")
    lastname.send_keys("Stanislawki")
    city = browser.find_element(By.CLASS_NAME, "city")
    city.send_keys("Kyiv")
    country = browser.find_element(By.ID, "country")
    country.send_keys("Ukraine")
    button = browser.find_element(By.ID, "submit_button")
    button.click()
    time.sleep(10)

finally:
    browser.quit()