from selenium import webdriver
from Pages.LoginPage import LoginPage

link = "https://b2b-ov.agora.ru/accounts/login/"

def test_error_checkbox(browser):
    login_page = LoginPage(browser, link)
    login_page.open()

    login_page.send_form_withoit_checkbox("123", "123")
    login_page.check_checkbox_empty()

def test_error_login(browser):
    login_page = LoginPage(browser, link)
    login_page.open()

    login_page.send_form_withoit_login("123")
    login_page.check_login_empty()

def test_error_password(browser):
    login_page = LoginPage(browser, link)
    login_page.open()

    login_page.send_form_withoit_password("123")
    login_page.check_password_empty()
