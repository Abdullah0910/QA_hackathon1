import json
import os
import pathlib
import time
from pages.login_page import LoginPage
from utils.driver_factory import get_driver
import os
from dotenv import load_dotenv
import pytest
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.common.action_chains import ActionChains
from pages.alert_page import AlertPage
from utils.driver_factory import get_driver


load_dotenv()


def test_valid_login():
    driver = get_driver()
    driver.get("https://the-internet.herokuapp.com/login")

    login = LoginPage(driver)
    login.enter_username("tomsmith ")
    login.enter_password("SuperSecretPassword!")
    login.click_login()

    assert "You logged into a secure area!" in login.get_flash_message()
    driver.quit()

def test_invalid_login():
    driver = get_driver()
    driver.get("https://the-internet.herokuapp.com/login")

    login = LoginPage(driver)
    login.enter_username("wronguser")
    login.enter_password("wrongpass")
    login.click_login()

    assert "Your username is invalid!" in login.get_flash_message()
    driver.quit()
class TestLinkChrome:
    def load_params_from_json(json_path):
        with open(json_path) as f:
            return json.load(f)

    @pytest.mark.parametrize("driver", load_params_from_json(str(pathlib.Path(__file__).parent.parent) + "/configurations.json"), indirect=True)
    def test_title(self, driver):
        
        """
        Verify item submission
        :return: None
        """