
# from pages.base_page import BasePage
# from locators.elements_page_locators import TextBoxPageLocators
from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'http://localhost/litecart/create_account')
            text_box_page.open()
            text_box_page.fill_textboxes()


# def test(driver):
#     page = BasePage(driver, 'http://localhost/litecart/create_account')
#     locator_1 = TextBoxPageLocators()
#     page.open()
#     page.element_is_visible(locator_1.COMPANY)
#     time.sleep(5)

