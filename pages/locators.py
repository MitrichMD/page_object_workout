from selenium.webdriver.common.by import By


# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    REGISTER_FORM = (By.ID, 'register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSW_1ST_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_PASSW_2ND_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BUTTON_SUBMIT = (By.CSS_SELECTOR, '#register_form > button')

class ProductPageLocators():
    ADDTOBASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRODUCT_ADDED_MSG = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs>span>a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET_ELEMENT = (By.CSS_SELECTOR, "#content_inner > p")
    FILLED_BASKET_ELEMENT = (By.CSS_SELECTOR, ".basket_summary")
