from .BasePage import BasePage
from .Locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        
    # Переходим на активную вкладку, если ссылка открылась в новом окне
        if len(self.browser.window_handles) > 1:
            i = len(self.browser.window_handles) - 1
            self.browser.switch_to.window(self.browser.window_handles[i])