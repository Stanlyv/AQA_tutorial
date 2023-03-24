# Чтобы указать язык браузера с помощью WebDriver, используйте класс Options и метод add_experimental_option, как указано в примере ниже:

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

# Для Firefox объявление нужного языка будет выглядеть немного иначе:

fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(firefox_profile=fp)


______


эта структура устарела:

fp = webdriver.FirefoxProfile()

fp.set_preference("intl.accept_languages", user_language)

актуальном считается вот это:

from selenium.webdriver.firefox.options import Options

options = Options()
options.set_preference("intl.accept_languages", user_language)
driver_browser = webdriver.Firefox(options=options)

