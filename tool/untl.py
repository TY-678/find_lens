from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExcuteOnSafari:
    def __init__(self):
        self.driver = webdriver.Safari()

    def open_url(self, url: str):
        self.driver.get(url)

    def find_element_by_xpath(self, xpath: str):
        element = self.driver.find_element(By.XPATH, xpath)
        return element

    def input_text(self, element, text: str | int):
        element.send_keys(text)

    def press_entrt(self, element):
        element.send_keys(Keys.RETURN)

    def click_element(self, element):
        element.click()

    def get_text(self, element):
        text = element.text
        return str(text)

    def wait_elwmwnt_visible(self, xpath: str, timeout: int):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(By.XPATH, xpath)
        )
        return element

    def waitVisibleAndClick(self, xpath: str, timeout: int):
        element = self.wait_elwmwnt_visible(xpath, timeout)
        self.click_element(element)
