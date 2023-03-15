import test
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math



link = "https://stepik.org/lesson/236895/step/1"


@pytest.fixture(scope="session")
def browser():
    print("\nBrowser opening")
    browser = webdriver.Chrome()
    print("\nBrowser opened")
    yield browser
    print("\nBrowser closing")
    browser.quit()
    print("\nBrowser closed")


def test_auth(browser):
    browser.get(link)
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "ember33"))
    )
    button.click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.NAME, "login")))
    browser.find_element(By.NAME, "login").send_keys(f"{test.email}")
    browser.find_element(By.NAME, "password").send_keys(f"{test.password}")
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "quiz__typename")))
    print("\nUser is logged in!")


@pytest.mark.parametrize("links", ["236895", "236896", "236897", "236898",
                                   "236899", "236903", "236904", "236905"])
def test_get_result(browser, links):
    def timezone():
        # answer = math.log(int(time.time()))
        # return answer + 2.3
        return "test_answer"
    time.sleep(2)
    links_go = f"https://stepik.org/lesson/{links}/step/1"
    print(f"links_go get value: {links}")
    browser.get(links_go)
    print(f"Opened link: {links}")
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "string-quiz__textarea"))
    )
    try: #этот трай надо заменить на что-то, что будет работать. Сейчас нажимает на ретрай после правильного ответа
        browser.implicitly_wait(3)
        browser.find_element(By.CLASS_NAME, "again-btn").click()
        browser.find_element(By.XPATH, "//button[text()='OK']").click()
    finally:
        time.sleep(1)
        browser.find_element(By.CLASS_NAME, "string-quiz__textarea").send_keys(math.log(int(time.time())))
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "smart-hints__hint"))
        )
        answer_text = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        print(f"\nText from responce: {answer_text.text}")
