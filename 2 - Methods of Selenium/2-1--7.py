from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    print("X = ", x)
    value = str(math.log(abs(12*math.sin(int(x)))))
    print("value = ", value)

    browser.find_element(By.ID, "answer").send_keys(value)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(5)

finally:
    browser.quit()