from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Stanley")
    browser.find_element(By.NAME, "lastname").send_keys("Stanislaw")
    browser.find_element(By.NAME, "email").send_keys("email")
    directory = os.path.abspath(os.path.dirname(__file__))
    directoryneed = os.path.split(directory)
    filepath = os.path.join(directoryneed[0], "tips.txt")
    print("filepath = ", filepath)


    browser.find_element(By.NAME, "file").send_keys(filepath)

    browser.find_element(By.CLASS_NAME, "btn").click()

    time.sleep(5)
finally:
    browser.quit()