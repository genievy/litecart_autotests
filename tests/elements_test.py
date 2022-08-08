from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'http://localhost/litecart/create_account')
            text_box_page.open()
            text_box_page.fill_textboxes()
            text_box_page.check_filled_form()
            print(text_box_page.check_filled_form())


        # def test_input_proposed_password(self, driver):
        #     text_box_page = TextBoxPage(driver, 'http://localhost/litecart/create_account')
        #     text_box_page.open()
        #     text_box_page.