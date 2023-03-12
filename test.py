from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/wait1.html"

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)
browser.find_element(By.ID, "verify").click()
time.sleep(5)