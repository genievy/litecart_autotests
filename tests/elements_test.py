import allure

from pages.elements_page import TextBoxPage, AuthBoxPage


@allure.suite("Test elements")
class TestElements:
    @allure.feature('Testing the registration page')
    class TestRegPage:

        @allure.title('Testing of filling out registration text boxes')
        def test_registration_textboxes(self, driver):
            text_box_page = TextBoxPage(driver, 'http://localhost/litecart/create_account')
            text_box_page.open()
            assert text_box_page.fill_textboxes() == text_box_page.check_filled_form(), 'Inputs do not match outputs'

        @allure.feature('Testing of filling out registration checkboxes')
        def test_registration_checkboxes(self, driver):
            text_box_page = TextBoxPage(driver, 'http://localhost/litecart/create_account')
            text_box_page.open()
            text_box_page.reg_switch_checkboxes()
            checkbox_1, checkbox_2 = text_box_page.reg_checkbox_condition()
            assert checkbox_1 == 'true', 'Checkbox 1 isn`t marked'
            assert checkbox_2 == 'true', 'Checkbox 2 isn`t marked'

    @allure.feature('Testing the authentication page')
    class TestAuthPage:

        @allure.feature('Testing of filling out authentication text boxes')
        def test_authentication_textboxes(self, driver):
            text_box_page = AuthBoxPage(driver, 'http://localhost/litecart')
            text_box_page.open()
            assert text_box_page.fill_auth_box() == text_box_page.check_auth_form(), 'Inputs do not match outputs'

        @allure.feature('Testing of checking out authentication checkboxes')
        def test_authentication_checkboxes(self, driver):
            text_box_page = AuthBoxPage(driver, 'http://localhost/litecart')
            text_box_page.open()
            text_box_page.auth_switch_checkboxes()
            checkbox_output = text_box_page.auth_checkbox_condition()
            assert checkbox_output == 'true', 'Checkbox isn`t marked'
