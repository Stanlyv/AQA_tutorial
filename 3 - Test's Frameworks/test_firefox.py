from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox()

driver.implicitly_wait(10)

def test_ff():
    driver.get("https://stepik.org/lesson/25969/step/8")

    driver.quit()