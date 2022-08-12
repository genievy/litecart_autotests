from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # create account
    COOKIES = (By.CSS_SELECTOR, "[name='accept_cookies']")
    COMPANY = (By.CSS_SELECTOR, "[name='company']")
    TAX_ID = (By.CSS_SELECTOR, "[name='tax_id']")
    FIRST_NAME = (By.CSS_SELECTOR, "[name='firstname']")
    LAST_NAME = (By.CSS_SELECTOR, "[name='lastname']")
    ADDRESS_1 = (By.CSS_SELECTOR, "[name='address1']")
    ADDRESS_2 = (By.CSS_SELECTOR, "[name='address2']")
    POSTAL_CODE = (By.CSS_SELECTOR, "input.form-control[name='postcode']")
    CITY = (By.CSS_SELECTOR, "[name='city']")
    COUNTRY_SELECT = (By.CSS_SELECTOR, "select.form-control[name='country_code']")
    ZONE_STATE_PROVINCE = (By.CSS_SELECTOR, "select.form-control[name='zone_code']")
    EMAIL = (By.XPATH, "//*[@id='box-create-account']/form/div[6]/div[1]/div/input")
    PHONE = (By.CSS_SELECTOR, "[name='phone']")
    DESIRED_PASSWORD = (By.XPATH, "/html/body/div/main/div[2]/section/form/div[7]/div[1]/div/input")
    CONFIRM_PASSWORD = (By.XPATH, "/html/body/div/main/div[2]/section/form/div[7]/div[2]/div/input")
    COUNTRY_OPTION = (By.CSS_SELECTOR, "select.form-control[value='BY']")
    CAPTCHA = (By.CSS_SELECTOR, "[name='captcha']")
    CHECKBOX_1 = (By.CSS_SELECTOR, "[name='newsletter']")
    CHECKBOX_1_JS = "[name=newsletter]"  # javascript-locator
    CHECKBOX_2 = (By.CSS_SELECTOR, "[name='terms_agreed']")
    CAPTCHA_ALERT = (By.CSS_SELECTOR, ".alert.alert-danger")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[value='Create Account']")
    NAME_OWNER = (By.CSS_SELECTOR, "li.account.dropdown>a")

class AuthBoxPageLocators:
    # sign_in
    SIGN_IN_DROPDOWN = (By.CSS_SELECTOR, "li.account.dropdown")
    EMAIL = (By.CSS_SELECTOR, "form[name='login_form']>div.form-group.required>div>input")
    PASSWORD = (By.XPATH, "//i[@class='fa fa-key fa-fw']/../..//input")
    CHECKBOX = (By.CSS_SELECTOR, "[name='remember_me']")
    CHECKBOX_JS = "[name=remember_me]"  # javascript-locator
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".btn-group.btn-block>.btn.btn-default")

