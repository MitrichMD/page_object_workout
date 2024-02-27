from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.FILLED_BASKET_ELEMENT), \
            "There's something in the basket, but should not be"

    def should_be_basketempty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_ELEMENT), 'No "Basket empty" text!'