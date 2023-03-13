from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class Testform(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        text = "Congratulations! You have successfully registered!"

        try:
            browser = webdriver.Chrome()
            browser.get(link)
            time.sleep(1)

            # requirement fields
            req = browser.find_elements(By.CSS_SELECTOR, "[required]")
            for i in req:
                i.send_keys("some text")

            browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
            time.sleep(1)

            self.assertEqual(text, browser.find_element(By.XPATH, "//h1").text)

            print(browser.find_element(By.XPATH, "//h1").text)
        finally:
            browser.quit()

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        text = "Congratulations! You have successfully registered!"

        try:
            browser = webdriver.Chrome()
            browser.get(link)
            time.sleep(1)

            # requirement fields
            browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys("Stan")
            browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys("Stanislaw")
            browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys("email")

            browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
            time.sleep(1)

            self.assertEqual(text, browser.find_element(By.XPATH, "//h1").text)

            print(browser.find_element(By.XPATH, "//h1").text)
        finally:
            browser.quit()

if __name__ == "__main__":
    unittest.main()