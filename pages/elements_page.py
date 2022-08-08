from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage
import time


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_textboxes(self):
        self.element_is_visible(self.locators.COMPANY).send_keys('Company')
        self.element_is_visible(self.locators.TAX_ID).send_keys('2346556')
        self.element_is_visible(self.locators.FIRST_NAME).send_keys('Oleg')
        self.element_is_visible(self.locators.LAST_NAME).send_keys('Kuznec')
        self.element_is_visible(self.locators.ADDRESS_1).send_keys('Gogol, 27')
        self.element_is_visible(self.locators.ADDRESS_2).send_keys('Gogol, 27')
        self.element_is_visible(self.locators.POSTAL_CODE).send_keys('109112')
        self.element_is_visible(self.locators.CITY).send_keys('Moscow')
        self.element_is_visible(self.locators.EMAIL).send_keys('wqwerq@qwdfer.qwet')
        self.element_is_visible(self.locators.PHONE).send_keys('+79429899889')
        self.action_move_to_element(self.element_is_visible(self.locators.DESIRED_PASSWORD))
        self.action_click_and_hold(self.element_is_visible(self.locators.DESIRED_PASSWORD))
        time.sleep(1)
        self.action_release(self.element_is_visible(self.locators.DESIRED_PASSWORD))
        self.element_is_visible(self.locators.DESIRED_PASSWORD).send_keys('auSrL3iW3wzCkRk')
        self.element_is_presence(self.locators.CONFIRM_PASSWORD).send_keys('auSrL3iW3wzCkRk')
        self.element_is_visible(self.locators.CAPTCHA).send_keys('5432')
        self.element_is_visible(self.locators.CHECKBOX_1).click()
        self.element_is_visible(self.locators.CHECKBOX_2).click()
        self.go_to_element(self.element_is_visible(self.locators.CREATE_ACCOUNT_BUTTON))
        # print(self.element_is_visible(self.locators.CREATE_ACCOUNT_BUTTON))
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