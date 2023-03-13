from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)

    Select(browser.find_element(By.ID, "dropdown")).select_by_value(str(x))

    browser.find_element(By.CLASS_NAME, "btn").click()

    time.sleep(5)

finally:
    browser.quit()