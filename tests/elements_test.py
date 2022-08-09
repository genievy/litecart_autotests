from pages.elements_page import TextBoxPage
from pages.elements_page import AuthBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'http://localhost/litecart/create_account')
            text_box_page.open()
            text_box_page.fill_textboxes()
            text_box_page.check_filled_form()
            print(text_box_page.check_filled_form())

    class TestAuthBox:

        def test_auth_box(self, driver):
            text_box_page = AuthBoxPage(driver, 'http://localhost/litecart')
            text_box_page.open()
            text_box_page.fill_auth_box()
            text_box_page.check_auth_form()
            print(text_box_page.check_auth_form())

