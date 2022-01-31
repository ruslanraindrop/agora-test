from selenium import webdriver
from Pages.LoginPage import LoginPage

link = "https://b2b-ov.agora.ru/accounts/login/"

def test_invalid_auth(browser):
    login_page = LoginPage(browser, link)
    login_page.open()

    # Отправляем некорректные данные и проверяем
    login_page.send_full_form("example", "example")
    login_page.should_be_error_alert()

def test_valid_auth(browser):
    login_page = LoginPage(browser, link)
    login_page.open()

    # Отправляем корректные данные и проверяем
    login_page.send_full_form("test12345@test.ru", "1234")
    login_page.should_be_catalog_url()
    login_page.should_be_auth_user_sidebar()