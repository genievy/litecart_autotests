from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        return self.driver.get(self.url)

    def find_element(self, element):
        self.driver.find_element(element)

    # Expected_conditions func
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


    # Execute_script func
    def checbox_switch(self, js_locator):
        scrpt = f'document.querySelector("{js_locator}").checked = true'
        self.driver.execute_script(scrpt)

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def title_is(self):
        self.driver.execute_script("return document.querySelectorAll('title')[0]")

    def go_to_page_down(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


    # ActionChains func
    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def action_left_click(self, element):
        action = ActionChains(self.driver)
        action.click(element)
        action.perform()

    def action_click_and_hold(self, element):
        action = ActionChains(self.driver)
        action.click_and_hold(element)
        action.perform()

    def action_release(self, element):
        action = ActionChains(self.driver)
        action.release(element)
        action.perform()