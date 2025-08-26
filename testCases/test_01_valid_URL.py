from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By

class TestValidURL:
    logger = LogGen.loggen()


# Test Case 1: To verify whether the URL of the webpage is correct.
    def test_valid_url_loading(self,driver):
        self.logger.info("****** Test Case-1 : TestValidURL Started *****")
        self.logger.info("****** Verifying the validity of URL by checking the presence of Guvi Logo element *****")
        logo_xpath = (driver.find_element(By.XPATH, "//img[@class='⭐️rwl3jt-0 cursor-pointer guvi_logo']"))
        if logo_xpath.is_displayed():
            print("URL loaded successfully")
            self.logger.info("****** URL loaded successfully *****")
        else:
            print("URL not loaded successfully")
            driver.save_screenshot(".\\screenshots\\" + "test_valid_url_loading.png")
            self.logger.error("****** URL loading error *****")
        self.logger.info("****** Test Case-1 : TestValidURL Completed *****")

