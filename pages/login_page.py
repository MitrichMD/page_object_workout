from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert 'login' in url, "incorrect login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not exist"

    def register_new_user(self):
        fakemail = str(time.time()) + "@fakemail.org"
        element = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD)
        element.send_keys(fakemail)
        time.sleep(1)
        element = self.browser.find_element(*LoginPageLocators.REG_PASSW_1ST_FIELD)
        element.send_keys('ololo12345')
        time.sleep(1)
        element = self.browser.find_element(*LoginPageLocators.REG_PASSW_2ND_FIELD)
        element.send_keys('ololo12345')
        time.sleep(1)
        element = self.browser.find_element(*LoginPageLocators.REG_BUTTON_SUBMIT)
        element.click()
        time.sleep(3)
