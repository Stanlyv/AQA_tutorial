from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"
text = "Congratulations! You have successfully registered!"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    #requirement fields ANOTHER VERSION SELECTION AT 1.6-11
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys("Stan")
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys("Stanislaw")
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys("email")

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(1)

    assert text == browser.find_element(By.XPATH, "//h1").text

    print(browser.find_element(By.XPATH, "//h1").text)
finally:
    browser.quit()