from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"
text = "Congratulations! You have successfully registered!"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    #requirement fields
    req = browser.find_elements(By.CSS_SELECTOR, "[required]")
    for i in req:
        i.send_keys("some text")

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(1)

    assert text == browser.find_element(By.XPATH, "//h1").text

    print(browser.find_element(By.XPATH, "//h1").text)
finally:
    browser.quit()