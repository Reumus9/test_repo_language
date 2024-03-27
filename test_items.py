import time 
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_language(browser, language_name):
    browser.get(link)
    time.sleep(30)
    # проверяю наличие наличие кнопки на странице
    try:
        button = WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket"))) 
    except TimeoutException:
        print("кнопки корзины нет на странице")
        assert False
    if language_name=="fr": # если предпочтительный язык является французским, то проверяю соответствует ли текст на кнопке fr
        button_text = button.text
        assert button_text == "Ajouter au panier", "техт не совпадает"
    elif language_name!="fr":
        assert True # так как мы ранее проверили наличие кнопки, то в остальных случаях у нас True

