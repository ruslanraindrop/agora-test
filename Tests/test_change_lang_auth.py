from selenium import webdriver
from Pages.LoginPage import LoginPage

link = "https://b2b-ov.agora.ru/accounts/login/"

def test_change_language_to_en(browser):
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.change_language("en")
    login_page.should_be_lang_url("en")

def test_change_language_to_pt(browser):
    login_page = LoginPage(browser, link)
    login_page.open()

    login_page.change_language("pt")
    login_page.should_be_lang_url("pt")

def test_change_language_to_ru(browser):
    link = "https://b2b-ov.agora.ru/en/accounts/login/"
    login_page = LoginPage(browser, link)
    login_page.open()

    login_page.change_language("ru")
    login_page.should_be_lang_url("ru")

