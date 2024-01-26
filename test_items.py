from selenium.webdriver.common.by import By
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_has_addtobasket_button(browser):
    try:
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-add-to-baske")
    except:
        pytest.fail("Кнопка не найдена")
    finally:
        time.sleep(5)
