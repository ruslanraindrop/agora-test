from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_BUTTON = (By.XPATH, "//a[@href='/accounts/login'and @class='t-btn js-click-stat']")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".agora__login-panel")

    LOGIN_USERNAME = (By.ID, "id_username")
    LOGIN_PASSWORD = (By.ID, "id_password")
    LOGIN_CHECKBOX = (By.ID, "id_is_agree")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, ".btn.btn-primary.agora__login-panel-btn")
    
    AUTH_USERNAME = (By.XPATH, "//div[@class='profile-dropdown__sub-title' and @title='test12345@test.ru']")
    ERROR_ALERT = (By.CSS_SELECTOR, ".alert-danger")

    SELECTOR_LANGUAGE = (By.CSS_SELECTOR, ".__dropdown.__dropdown_mr.has-dropdown")
    SELECTOR_EN = (By.XPATH, "//span[contains(text(),'English')]/..")
    SELECTOR_PT = (By.XPATH, "//span[contains(text(),'Português Brasileiro')]/..")
    SELECTOR_RU = (By.XPATH, "//span[contains(text(),'Русский')]/..")