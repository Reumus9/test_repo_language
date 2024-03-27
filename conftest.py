# написать тест для проверки наличия кнопки корзины с определенным текстом на различных языках
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language")
    

from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_name})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def language_name(request):
    return request.config.getoption("language")






