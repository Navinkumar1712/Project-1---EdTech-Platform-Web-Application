import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver
from utilities.readProperties import ReadConfig


# Add a command-line option to select browser (default = Chrome)
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on (chrome, firefox, or edge)"
    )

# Fixture to launch and close the browser before/after each test
@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    driver = None

    # Choose browser based on user input
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # Setup: Launch browser and open application
    print("\n--- Setup: Launching browser ---")
    driver.get(ReadConfig.getApplicationURL())
    driver.maximize_window()

    yield driver  # Provide driver instance to test case

    # Teardown: Close browser after test execution
    print("--- Teardown: Closing browser ---")
    driver.quit()


########## Pytest HTML Report Customization #########

# Hook to add extra environment info in the HTML report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Project 1 - EdTech Platform Web Application'
    config.stash[metadata_key]['Module'] = 'GUVI Website'
    config.stash[metadata_key]['Tester Name'] = 'Navin Kumar M'

# Hook to remove unwanted environment info from the HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
