import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    chrome_binary_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

    # Create ChromeOptions and specify the binary location
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_binary_path

    # Initialize the Chrome WebDriver with the specified options
    driver = webdriver.Chrome(chrome_options)
    yield driver  # provide the webdriver instance to the test
    driver.quit()  # clean up after the test
