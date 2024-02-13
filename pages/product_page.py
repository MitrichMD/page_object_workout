from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADDTOBASKET_BUTTON)
        button.click()

    def should_be_addtobasket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADDTOBASKET_BUTTON), "Basket button is missing"

    def expected_result_1_added_product_is_correct(self):
        assert (self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE).text ==
                self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text), \
                '"After add" message and product title do not match!'

    def expected_result_2_basket_total_equals_product_price(self):
        assert (self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text ==
                self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text), \
            'Basket total and product price do not match!'
