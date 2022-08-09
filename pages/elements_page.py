from locators.elements_page_locators import TextBoxPageLocators
from locators.elements_page_locators import AuthBoxPageLocators
from pages.base_page import BasePage
from generators.generator import random_custumer
import time


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_textboxes(self):
        # person_info - переменная, которой присваивается значение ф-ции random_custumer()
        # всякий раз при обращении к ней
        custumer_info = next(random_custumer())
        # создаем набор значений для заполнения полей ввода (оптимизировать!)
        company = custumer_info.company
        tax_id = custumer_info.tax_id
        first_name = custumer_info.first_name
        last_name = custumer_info.last_name
        address_1 = custumer_info.address_2
        address_2 = custumer_info.company
        postal_code = custumer_info.postal_code
        city = custumer_info.city
        email = custumer_info.email
        phone = custumer_info.phone
        password = custumer_info.password
        captcha = custumer_info.captcha

        self.element_is_visible(self.locators.COMPANY).send_keys(company)
        self.element_is_visible(self.locators.TAX_ID).send_keys(tax_id)
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.ADDRESS_1).send_keys(address_1)
        self.element_is_visible(self.locators.ADDRESS_2).send_keys(address_2)
        self.element_is_visible(self.locators.POSTAL_CODE).send_keys(postal_code)
        self.element_is_visible(self.locators.CITY).send_keys(city)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.PHONE).send_keys(phone)
        self.action_move_to_element(self.element_is_visible(self.locators.DESIRED_PASSWORD))
        self.action_click_and_hold(self.element_is_visible(self.locators.DESIRED_PASSWORD))
        time.sleep(1)
        self.action_release(self.element_is_visible(self.locators.DESIRED_PASSWORD))
        self.element_is_visible(self.locators.DESIRED_PASSWORD).send_keys(password)
        self.element_is_presence(self.locators.CONFIRM_PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.CAPTCHA).send_keys(captcha)
        # "Включается" чек-бох, исполнением javascript-кода
        self.checkbox_switch(self.locators.CHECKBOX_1_JS)
        # "Включается" чек-бох, методом click()
        self.element_is_visible(self.locators.CHECKBOX_2).click()
        self.go_to_element(self.element_is_visible(self.locators.CREATE_ACCOUNT_BUTTON))
        # self.element_is_presence(self.locators.CREATE_ACCOUNT_BUTTON).click()
        time.sleep(3)

    def check_filled_form(self):
        company = self.element_is_visible(self.locators.COMPANY).get_attribute('value')
        tax_id = self.element_is_visible(self.locators.TAX_ID).get_attribute('value')
        first_name = self.element_is_visible(self.locators.COMPANY).get_attribute('value')
        last_name = self.element_is_visible(self.locators.LAST_NAME).get_attribute('value')
        adress1 = self.element_is_visible(self.locators.ADDRESS_1).get_attribute('value')
        adress2 = self.element_is_visible(self.locators.ADDRESS_2).get_attribute('value')
        postal_code = self.element_is_visible(self.locators.POSTAL_CODE).get_attribute('value')
        city = self.element_is_visible(self.locators.CITY).get_attribute('value')
        email = self.element_is_visible(self.locators.EMAIL).get_attribute('value')
        phone = self.element_is_visible(self.locators.PHONE).get_attribute('value')
        desired_password = self.element_is_visible(self.locators.DESIRED_PASSWORD).get_attribute('value')
        confirm_password = self.element_is_visible(self.locators.CONFIRM_PASSWORD).get_attribute('value')
        captcha = self.element_is_visible(self.locators.CAPTCHA).get_attribute('value')
        checkbox_1 = self.element_is_visible(self.locators.CHECKBOX_1).get_attribute('checked')
        checkbox_2 = self.element_is_visible(self.locators.CHECKBOX_2).get_attribute('checked')

        return company, tax_id, first_name, last_name, adress1, adress2, postal_code, email, city, phone, desired_password, confirm_password, captcha, checkbox_1, checkbox_2


class AuthBoxPage(BasePage):
    locators = AuthBoxPageLocators()

    def fill_auth_box(self):
        self.element_is_visible(self.locators.SIGN_IN_DROPDOWN).click()
        self.element_is_visible(self.locators.EMAIL).send_keys('test@test.test')
        self.element_is_visible(self.locators.PASSWORD).send_keys('Password123')
        self.checkbox_switch(self.locators.CHECKBOX_JS)
        # self.element_is_visible(self.locators.SIGN_IN_BUTTON).click()
        time.sleep(3)

    def check_auth_form(self):
        email = self.element_is_visible(self.locators.EMAIL).get_attribute('value')
        password = self.element_is_visible(self.locators.PASSWORD).get_attribute('value')
        checkbox = self.element_is_visible(self.locators.CHECKBOX).get_attribute('checked')

        return email, password, checkbox
