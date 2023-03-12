from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    findlink = browser.find_element(By.PARTIAL_LINK_TEXT, text)
    findlink.click()

    time.sleep(1)

    firstname = browser.find_element(By.NAME, "first_name")
    firstname.send_keys("Stanislav")
    print(firstname)
    lastname = browser.find_element(By.NAME, "last_name")
    lastname.send_keys("Stanislawki")
    print(lastname)
    city = browser.find_element(By.CLASS_NAME, "city")
    city.send_keys("Kyiv")
    print(city)
    country = browser.find_element(By.ID, "country")
    country.send_keys("Ukraine")
    print(country)
    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    print("button ", button)
    button.click()
    time.sleep(10)


finally:
    browser.quit()