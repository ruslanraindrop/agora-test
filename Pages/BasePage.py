from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

timeout = 20

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_correct_url(self, url):
        assert url == self.browser.current_url, f"Вместо {url}, открылась {self.browser.current_url}"

    def check_checkbox_validation_msg(self, how, what):
        # Проверка HTML5 валидации checkbox-элементов
        element = WebDriverWait(self.browser, timeout).until(ec.visibility_of_element_located((how, what))).get_attribute("validationMessage")
        if element == "Чтобы продолжить, установите этот флажок." or \
                element == "Check this box to continue." or \
                    element == "Para continuar, selecione esta caixa de seleção":
            return True
        else:
            return False

    def check_input_validation_msg(self, how, what):
        # Проверка HTML5 валидации checkbox-элементов
        element = WebDriverWait(self.browser, timeout).until(ec.visibility_of_element_located((how, what))).get_attribute("validationMessage")
        if element == "Заполните это поле." or \
                element == "Please fill in this field" or \
                    element == "Preencha este campo":
            return True
        else:
            return False