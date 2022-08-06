from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        return self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_invisibility(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_presence(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_presence(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def find_captcha(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def go_to_element(self, element):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)", element)

    # def get_element_properties(self, element):
    #     self.driver.execute_script('get.textContent', element)

    # def alert_is_present(self, timeout=5):
    #     return wait(self.driver, timeout).until(EC.alert_is_present())

    # def alert_switch(self):
    #     return self.driver.switch_to.alert

    # def finding_element(self, locator):
    #     self.driver.find_element(locator)
