from .Locators import LoginPageLocators
from .BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage): 
    def should_be_login_url(self):
        self.is_correct_url("https://b2b-ov.agora.ru/accounts/login/")

    def should_be_catalog_url(self):
        self.is_correct_url("https://b2b-ov.agora.ru/")

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "На странице нет формы авторизации"

    def should_be_error_alert(self):
        assert self.is_element_present(*LoginPageLocators.ERROR_ALERT), "На странице нет формы авторизации"

    def send_full_form(self, username, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_USERNAME).send_keys(username)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_CHECKBOX).click()
        self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT).click()

    def send_form_withoit_checkbox(self, username, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_USERNAME).send_keys(username)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT).click()

    def send_form_withoit_login(self, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_CHECKBOX).click()
        self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT).click()

    def send_form_withoit_password(self, username):
        self.browser.find_element(*LoginPageLocators.LOGIN_USERNAME).send_keys(username)
        self.browser.find_element(*LoginPageLocators.LOGIN_CHECKBOX).click()
        self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT).click()

    def should_be_auth_user_sidebar(self):
        assert self.is_element_present(*LoginPageLocators.AUTH_USERNAME), "На странице нет меню авторизованного пользователя"
    
    def change_language(self, lang):
        self.browser.find_element(*LoginPageLocators.SELECTOR_LANGUAGE).click()

        if lang == "en":
            self.browser.find_element(*LoginPageLocators.SELECTOR_EN).click()

        if lang == "pt":
            self.browser.find_element(*LoginPageLocators.SELECTOR_PT).click()

        if lang == "ru":
            self.browser.find_element(*LoginPageLocators.SELECTOR_RU).click()

    def should_be_lang_url(self, lang):
        if lang == "en":
            self.is_correct_url("https://b2b-ov.agora.ru/en/accounts/login/")

        if lang == "pt":
            self.is_correct_url("https://b2b-ov.agora.ru/pt-br/accounts/login/")

        if lang == "ru":
            self.is_correct_url("https://b2b-ov.agora.ru/accounts/login/")

    def check_checkbox_empty(self):
        assert self.check_checkbox_validation_msg(*LoginPageLocators.LOGIN_CHECKBOX), "Не соответствует ошибка у чекбокса"

    def check_login_empty(self):
        assert self.check_input_validation_msg(*LoginPageLocators.LOGIN_USERNAME), "Не соответствует ошибка у логина"
    
    def check_password_empty(self):
        assert self.check_input_validation_msg(*LoginPageLocators.LOGIN_PASSWORD), "Не соответствует ошибка у логина"