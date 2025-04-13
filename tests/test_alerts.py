import json
import os
import pathlib
import time

import pytest
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.common.action_chains import ActionChains
from pages.alert_page import AlertPage
from utils.driver_factory import get_driver

def test_js_alert():
    driver = get_driver()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(5)
    alerts = AlertPage(driver)
    alerts.trigger_js_alert()
    assert "You successfully clicked an alert" in alerts.get_result_text()
    driver.quit()
def test_js_alert():
    driver = get_driver()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(5)
    alerts = AlertPage(driver)
    alerts.trigger_js_alert()
    assert "You successfully clicked an alert" in alerts.get_result_text()
    driver.quit()

def test_js_confirm_accept():
    driver = get_driver()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(5)
    alerts = AlertPage(driver)
    alerts.trigger_js_confirm(accept=True)
    assert "You clicked: Ok" in alerts.get_result_text()
    driver.quit()

def test_js_confirm_dismiss():
    driver = get_driver()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(5)
    alerts = AlertPage(driver)
    alerts.trigger_js_confirm(accept=False)
    assert "You clicked: Cancel" in alerts.get_result_text()
    driver.quit()

def test_js_prompt_input():
    driver = get_driver()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(5)
    alerts = AlertPage(driver)
    alerts.trigger_js_prompt("Hello")
    assert "You entered: Hello" in alerts.get_result_text()
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
    