from .pages.login_page import LoginPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_page()
    time.sleep(5)
