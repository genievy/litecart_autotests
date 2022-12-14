
import allure

from locators.elements_page_locators import TextBoxPageLocators, AuthBoxPageLocators
from pages.base_page import BasePage
from generators.generator import random_custumer


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step("Registration. Filling out text boxes")
    def fill_textboxes(self):
        custumer_info = next(random_custumer())
        lista_input = [custumer_info.company,
                       custumer_info.tax_id,
                       custumer_info.first_name,
                       custumer_info.last_name,
                       custumer_info.address_1,
                       custumer_info.address_2,
                       custumer_info.postal_code,
                       custumer_info.city,
                       custumer_info.email,
                       custumer_info.phone,
                       custumer_info.password,
                       custumer_info.password,
                       custumer_info.captcha]
        with allure.step('filing fields'):
            self.element_visible(self.locators.COMPANY).send_keys(custumer_info.company)
            self.element_visible(self.locators.TAX_ID).send_keys(custumer_info.tax_id)
            self.element_visible(self.locators.FIRST_NAME).send_keys(custumer_info.first_name)
            self.element_visible(self.locators.LAST_NAME).send_keys(custumer_info.last_name)
            self.element_visible(self.locators.ADDRESS_1).send_keys(custumer_info.address_1)
            self.element_visible(self.locators.ADDRESS_2).send_keys(custumer_info.address_2)
            self.element_visible(self.locators.POSTAL_CODE).send_keys(custumer_info.postal_code)
            self.element_visible(self.locators.CITY).send_keys(custumer_info.city)
            self.element_visible(self.locators.EMAIL).send_keys(custumer_info.email)
            self.element_visible(self.locators.PHONE).send_keys(custumer_info.phone)
        with allure.step('Input password'):
            self.element_visible(self.locators.DESIRED_PASSWORD).send_keys(custumer_info.password)
            self.element_presence(self.locators.CONFIRM_PASSWORD).send_keys(custumer_info.password)
        with allure.step('Input captcha'):
            self.element_visible(self.locators.CAPTCHA).send_keys(custumer_info.captcha)
        return lista_input

    @allure.step("Registration. Checking the text fields")
    def check_filled_form(self):
        lista_output = [self.element_visible(self.locators.COMPANY).get_attribute('value'),
                        self.element_visible(self.locators.TAX_ID).get_attribute('value'),
                        self.element_visible(self.locators.FIRST_NAME).get_attribute('value'),
                        self.element_visible(self.locators.LAST_NAME).get_attribute('value'),
                        self.element_visible(self.locators.ADDRESS_1).get_attribute('value'),
                        self.element_visible(self.locators.ADDRESS_2).get_attribute('value'),
                        self.element_visible(self.locators.POSTAL_CODE).get_attribute('value'),
                        self.element_visible(self.locators.CITY).get_attribute('value'),
                        self.element_visible(self.locators.EMAIL).get_attribute('value'),
                        self.element_visible(self.locators.PHONE).get_attribute('value'),
                        self.element_visible(self.locators.DESIRED_PASSWORD).get_attribute('value'),
                        self.element_visible(self.locators.CONFIRM_PASSWORD).get_attribute('value'),
                        self.element_visible(self.locators.CAPTCHA).get_attribute('value')]
        return lista_output

    @allure.step("Registration. Switching check-boxes")
    def reg_switch_checkboxes(self):
        with allure.step('Registration. Switch check-boxes'):
            self.go_to_page_down()
            # self.checkbox_switch(self.locators.CHECKBOX_1_JS)
            self.element_visible(self.locators.CHECKBOX_1).click()
            self.element_visible(self.locators.CHECKBOX_2).click()

    @allure.step("Registration. Checking check-boxes conditions")
    def reg_checkbox_condition(self):
        with allure.step('Registration. Checking check-boxes'):
            checkbox_1 = self.element_visible(self.locators.CHECKBOX_1).get_attribute('checked')
            checkbox_2 = self.element_visible(self.locators.CHECKBOX_2).get_attribute('checked')
        return checkbox_1, checkbox_2


class AuthBoxPage(BasePage):
    locators = AuthBoxPageLocators()

    @allure.step("Authentication. Filling out text boxes")
    def fill_auth_box(self):
        custumer_info = next(random_custumer())
        lista_input = [custumer_info.email,
                       custumer_info.password]
        self.element_visible(self.locators.SIGN_IN_DROPDOWN).click()
        self.element_visible(self.locators.EMAIL).send_keys(custumer_info.email)
        self.element_visible(self.locators.PASSWORD).send_keys(custumer_info.password)
        return lista_input

    @allure.step("Authentication. Checking the text fields")
    def check_auth_form(self):
        lista_output = [self.element_visible(self.locators.EMAIL).get_attribute('value'),
                        self.element_visible(self.locators.PASSWORD).get_attribute('value')]
        return lista_output

    @allure.step("Authentication. Switching check-boxes")
    def auth_switch_checkboxes(self):
        self.element_visible(self.locators.SIGN_IN_DROPDOWN).click()
        self.checkbox_switch(self.locators.CHECKBOX_JS)

    @allure.step("Authentication. Checking check-boxes conditions")
    def auth_checkbox_condition(self):
        return self.element_visible(self.locators.CHECKBOX).get_attribute('checked')
