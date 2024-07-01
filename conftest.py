# написать тест для проверки наличия кнопки корзины с определенным текстом на различных языках
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as foxoptions


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language")
    
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")



@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        browser = webdriver.Chrome(options=options)
        yield browser
        browser.quit()
    elif browser_name == "firefox":
    
        fp = foxoptions()
        fp.set_preference("intl.accept_languages", browser_language)
        browser = webdriver.Firefox(options=fp)
        yield browser
        browser.quit()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

@pytest.fixture(scope="function")
def language_name(request):
    return request.config.getoption("language")






