from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By


class TestBtnVisibility:
    logger = LogGen.loggen()

    def test_visible_login_btn(self, driver):
        self.logger.info("****** Test Case-3 : Test Visibility of Login Button Started *****")
        self.lp = LoginPage(driver)
        try:
            # Find Login button
            login_btn = driver.find_element(By.ID, self.lp.btn_login_id)

            # Check if button is visible and clickable
            if login_btn.is_displayed() and login_btn.is_enabled():
                print("The Login button is displayed and enabled.")
                self.logger.info("****** Login Button Visible and Clickable *****")

                # Click login button
                login_btn.click()

                # Verify URL
                current_url = driver.current_url
                assert current_url == "https://www.guvi.in/sign-in/"
                self.logger.info("****** Successfully landed on Login Page *****")

                # Verify page title
                print(driver.title)
                assert driver.title == "GUVI | Login"
                self.logger.info("****** Login Page Title Verified *****")

            else:
                # Save screenshot if button not clickable
                self.logger.info("****** Login Button not visible/clickable *****")
                driver.save_screenshot(".\\screenshots\\" + "test_visible_login_btn.png")
                print("The Login button is not displayed or disabled")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            self.logger.info("****** Test Case-3 : Test Visibility of Login Button Completed *****")


