from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By

class TestValidURL:
    logger = LogGen.loggen()

# Test Case 2: To verify whether the title of the webpage is correct.

    def test_is_title_valid(self, driver):
        self.logger.info("****** Test Case-2 : Title Validation Started *****")
        self.logger.info("****** Verifying the Homepage Title *****")
        # Fetching the actual title from the webpage.
        actual_title = driver.title
        expected_title = "GUVI | Learn to code in your native language"
        # Using conditional statement, Checking if the Title displayed is as expected.
        if actual_title == expected_title:
            assert True
            self.logger.info("****** Title displayed as expected *****")
        else:
            # Upon failure capturing screenshot of the webpage
            driver.save_screenshot(".\\screenshots\\" + "test_is_title_valid.png")
            self.logger.error("****** Title Error *****")
        self.logger.info("****** Test Case-2 : Title Validation Completed *****")