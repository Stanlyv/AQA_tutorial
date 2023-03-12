from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    field = browser.find_elements(By.CSS_SELECTOR, "[type='text']")
    for i in field:
        i.send_keys("some text")

    browser.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(50)

finally:
    browser.quit()