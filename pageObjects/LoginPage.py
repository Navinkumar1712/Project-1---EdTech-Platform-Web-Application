from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Login page elements and actions are defined here
class LoginPage:
    # Locators for login page elements
    btn_login_id = "login-btn"
    textbox_email_id = "email"
    textbox_password_id = "password"
    btn_login_xpath = "//a[@id='login-btn']"
    btn_dropdown_xpath = "//div[@id='dropdown_title']"
    btn_sign_out_xpath = "//*[contains(text(), 'Sign Out')]"
    btn_signup_xpath = "//a[contains (text(), 'Sign up')]"
    btn_login_signup_xpath = "//a[contains (text(), 'Login')]"

    def __init__(self, driver):
        # Initialize the driver instance
        self.driver = driver

    def click_login_btn(self):
        # Click on the login button (homepage login)
        self.driver.find_element(By.ID, self.btn_login_id).click()

    def set_email(self, email):
        # Enter valid email into email textbox
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def set_password(self, password):
        # Enter valid password into password textbox
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def set_invalid_email(self, invalid_email):
        # Enter invalid email into email textbox (for negative testing)
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(invalid_email)

    def set_invalid_password(self, invalid_password):
        # Enter invalid password into password textbox (for negative testing)
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(invalid_password)

    def click_login(self):
        # Click on the login button (inside login form)
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_sign_out(self):
        # Wait for dropdown to appear and click on it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_dropdown_xpath))
        ).click()
        # Click on sign out option
        self.driver.find_element(By.XPATH, self.btn_sign_out_xpath).click()


