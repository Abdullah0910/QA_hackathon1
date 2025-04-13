from selenium.webdriver.common.by import By

class AlertPage:
    def __init__(self, driver):
        self.driver = driver
        self.js_alert = (By.XPATH, "//button[text()='Click for JS Alert']")
        self.js_confirm = (By.XPATH, "//button[text()='Click for JS Confirm']")
        self.js_prompt = (By.XPATH, "//button[text()='Click for JS Prompt']")
        self.result = (By.ID, "result")

    def trigger_js_alert(self):
        self.driver.find_element(*self.js_alert).click()
        alert = self.driver.switch_to.alert
        alert.accept()

    def trigger_js_confirm(self, accept=True):
        self.driver.find_element(*self.js_confirm).click()
        alert = self.driver.switch_to.alert
        if accept:
            alert.accept()
        else:
            alert.dismiss()

    def trigger_js_prompt(self, text=None):
        self.driver.find_element(*self.js_prompt).click()
        alert = self.driver.switch_to.alert
        if text:
            alert.send_keys(text)
        alert.accept()

    def get_result_text(self):
        return self.driver.find_element(*self.result).text
