from selenium import webdriver
from Pages.MainPage import MainPage
from Pages.LoginPage import LoginPage

link = "https://b2b-ov.agora.ru/"

def test_main_page_to_login(browser):
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()

    # Инициализируем страницу авторизации
    login_page = LoginPage(browser, browser.current_url)

    # Проверяем, что открылся нужный URL с формой авторизации
    login_page.should_be_login_url()
    login_page.should_be_login_form()
