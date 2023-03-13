from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "btn").click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)
    x = browser.find_element(By.ID, "input_value").text
    value = str(math.log(abs(12 * math.sin(int(x)))))
    browser.find_element(By.ID, "answer").send_keys(value)
    browser.find_element(By.CLASS_NAME, "btn").click()
    text = browser.switch_to.alert.text
    num = text.split(": ")[-1]
    print(num)

    time.sleep(5)
finally:
    browser.quit()