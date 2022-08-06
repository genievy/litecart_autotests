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
        self.element_is_visible(self.locators1.POSTAL_CODE).send_keys('176789')
        self.element_is_visible(self.locators1.CITY).send_keys('Moscow')
        # self.element_is_visible(self.locators1.COUNTRY_SELECT).click()
        # self.element_is_visible(self.locators1.COUNTRY_OPTION).click()
        # self.element_is_visible(self.locators1.ZONE_STATE_PROVINCE).send_keys('qerqw')
        self.element_is_visible(self.locators1.EMAIL).send_keys('qwe@qwe.qwe')
        self.element_is_visible(self.locators1.PHONE).send_keys('+79453456789')
        self.element_is_visible(self.locators1.DESIRED_PASSWORD).send_keys('auSrL3iW3wzCkRk')
        self.element_is_presence(self.locators1.CONFIRM_PASSWORD).send_keys('auSrL3iW3wzCkRk')
        self.element_is_visible(self.locators1.CAPTCHA).send_keys('5432')
        self.element_is_visible(self.locators2.CHECKBOX_1).click()
        self.element_is_visible(self.locators2.CHECKBOX_2).click()
        self.go_to_element(self.locators3.CREATE_ACCOUNT_BUTTON)
        self.element_is_presence(self.locators3.CREATE_ACCOUNT_BUTTON).click()
        # self.alert_is_present()
        time.sleep(1)


    def check_alert(self):
        try:
            text_alert = self.find_captcha(self.locators4.CAPTCHA_ALERT).get_attribute('textContent')
            if text_alert.strip() == "Invalid CAPTCHA given":
                print(text_alert.strip())
        except:
            print("Invalid input data")