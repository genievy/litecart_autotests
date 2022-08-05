from locators.elements_page_locators import TextBoxPageLocators
from locators.elements_page_locators import CheckBoxPageLocators
from locators.elements_page_locators import ButtonsPageLocators
from locators.elements_page_locators import AlertPageLocators
from pages.base_page import BasePage
import time


class TextBoxPage(BasePage):
    locators1 = TextBoxPageLocators()
    locators2 = CheckBoxPageLocators()
    locators3 = ButtonsPageLocators()
    locators4 = AlertPageLocators()

    def fill_textboxes(self):
        self.element_is_visible(self.locators1.COMPANY).send_keys('Company')
        self.element_is_visible(self.locators1.TAX_ID).send_keys('1234567890')
        self.element_is_visible(self.locators1.FIRST_NAME).send_keys('Oleg')
        self.element_is_visible(self.locators1.LAST_NAME).send_keys('Kuznetsov')
        self.element_is_visible(self.locators1.ADDRESS_1).send_keys('Gogolya, 7')
        self.element_is_visible(self.locators1.ADDRESS_2).send_keys('Gogolya, 7')
        self.element_is_visible(self.locators1.POSTAL_CODE).send_keys('109112')
        self.element_is_visible(self.locators1.CITY).send_keys('Moscow')
        # self.element_is_visible(self.locators1.COUNTRY_SELECT).click()
        # self.element_is_visible(self.locators1.COUNTRY_OPTION).click()
        # self.element_is_visible(self.locators1.ZONE_STATE_PROVINCE).send_keys('qerqw')
        self.element_is_visible(self.locators1.EMAIL).send_keys('qwe@qwe.qwe')
        self.element_is_visible(self.locators1.PHONE).send_keys('+79453456789')
        self.element_is_visible(self.locators1.DESIRED_PASSWORD).send_keys('auSrL3iW3wzCkRk')
        time.sleep(3)
        self.element_is_presence(self.locators1.CONFIRM_PASSWORD).send_keys('auSrL3iW3wzCkRk')
        self.element_is_visible(self.locators1.CAPTCHA).send_keys('5432')
        self.element_is_visible(self.locators2.CHECKBOX_1).click()
        self.element_is_visible(self.locators2.CHECKBOX_2).click()
        self.element_is_visible(self.locators3.CREATE_ACCOUNT_BUTTON).click()

        if self.find_element(self.locators4.CAPTCHA_ALERT).get_attribute('textContent') == "\n  \n   Invalid CAPTCHA given\n":
            print("Invalid CAPTCHA given")
        else:
            print("Invalid input data")

        time.sleep(25)