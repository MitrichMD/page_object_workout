from .pages.product_page import ProductPage
import time


# def test_page_has_addtobasket_button(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_addtobasket_button()
#     time.sleep(2)

def test_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.expected_result_1_added_product_is_correct()
    page.expected_result_2_basket_total_equals_product_price()
    time.sleep(5)
