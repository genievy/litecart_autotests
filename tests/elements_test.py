import allure

from pages.elements_page import TextBoxPage, AuthBoxPage


@allure.suite("Test elements")
class TestElements:
    @allure.feature('Testing the registration page')
    class TestRegPage:

        @allure.title('Testing of filling out registration text boxes')
        def test_registration_text_boxes(self, driver):
            text_box_page = TextBoxPage(driver, 'http://localhost/litecart/create_account')
            text_box_page.open()
            assert text_box_page.fill_textboxes() == text_box_page.check_filled_form(), 'Inputs do not match outputs'

        def test_registration_check_boxes(self, driver):
            pass

    @allure.feature('Testing the authentication page')
    class TestAuthPage:
        @allure.feature('Testing of filling out authentication text boxes')
        def test_auth_box(self, driver):
            text_box_page = AuthBoxPage(driver, 'http://localhost/litecart')
            text_box_page.open()
            text_box_page.fill_auth_box()
            text_box_page.check_auth_form()
            print(text_box_page.check_auth_form())
