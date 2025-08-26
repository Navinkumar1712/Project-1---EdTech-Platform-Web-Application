from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By


class TestBtnVisibility:
    logger = LogGen.loggen()


# Test Case 4 - To verify visibility and clickable feature of the Sign-Up button.

    def test_visible_signup_btn(self, driver):
        self.logger.info("****** Test Case-4 : Test Visibility of Sign up Button Started *****")
        self.lp = LoginPage(driver)
        try:
            # Locate the Sign up button element
            sign_up_btn = driver.find_element(By.XPATH,self.lp.btn_signup_xpath)
            # Check if the Sign up button is displayed and enabled
            if sign_up_btn.is_displayed() and sign_up_btn.is_enabled():
                print("The Sign up button is displayed.")
                self.logger.info("****** Sign up Button Visible and Clickable *****")
                # Perform actions on the enabled button, e.g., click
                sign_up_btn.click()
                current_url = driver.current_url
                assert current_url == "https://www.guvi.in/register/"
                print("Successfully landed on Register Page upon clicking Sign up Button")
                print(driver.title)
                assert driver.title == "GUVI | Sign Up"
                self.logger.info("****** On Clicking Sign up Button, it navigates to Register Page *****")
            else:
                self.logger.info("****** Sign up Button Not Visible and Clickable *****")
                driver.save_screenshot(".\\screenshots\\" + "test_visible_signup_btn.png")
                print("The Sign up button is not displayed or it is disabled.")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
           self.logger.info("****** Test Case-4 : Test Visibility of Sign up Button Completed *****")

# Test Case 5 - To verify navigation to the Sign-In page via the Sign-Up button.

    def test_login_btn_signup(self, driver):
        self.logger.info("****** Test Case-5 : Verifying the navigation to the Sign-In page via the Sign-Up button Started *****")
        self.lp = LoginPage(driver)
        try:
            # Locate the Sign up button element
            sign_up_btn = driver.find_element(By.XPATH,self.lp.btn_signup_xpath)
            sign_up_btn.click()
            current_url = driver.current_url
            assert current_url == "https://www.guvi.in/register/"
            # Locate Login button on Register page and click on it
            login_sign_up_btn = driver.find_element(By.XPATH,self.lp.btn_login_signup_xpath)
            if login_sign_up_btn.is_enabled():
                print("The Login button is enabled in Register page.")
                login_sign_up_btn.click()
                current_url = driver.current_url
                assert current_url == "https://www.guvi.in/sign-in/"
                print("Successfully landed on Login Page upon clicking Login button via Sign up")
                print(driver.title)
                assert driver.title == "GUVI | Login"
                self.logger.info("****** Login from Register Page verified *****")
            else:
                print("The Sign up button is not displayed or it is disabled.")
                driver.save_screenshot(".\\screenshots\\" + "test_login_btn_signup.png")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            self.logger.info("****** Test Case-5 : Verifying the navigation to the Sign-In page via the Sign-Up button Completed *****")