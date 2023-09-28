import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

"""
chrome_binary_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

# Create ChromeOptions and specify the binary location
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_binary_path

# Initialize the Chrome WebDriver with the specified options"""


# driver = webdriver.Chrome(chrome_options)

@pytest.mark.login
def test_login(driver):
    url = "https://www.saucedemo.com/v1/"
    driver.get(url)

    csv_file_path = '/Users/somud/PycharmProjects/pythonProject1/data_driven_framework/test_data/testdata.csv'
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for data in reader:
            username = data['username']
            password = data['password']

            driver.find_element(By.NAME, "user-name").send_keys(username)
            driver.find_element(By.NAME, "password").send_keys(password)
            driver.find_element(By.ID, "login-button").click()
            time.sleep(5)
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="product_label"]')))
            txt_to_verify = element.text
            if txt_to_verify == "Products":
                print("successful page login")
            else:
                print("login unsuccessful")
            button = driver.find_element(By.XPATH, '//div[@class="bm-burger-button"]')
            button.click()
            time.sleep(3)
            driver.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]').click()
            time.sleep(2)

