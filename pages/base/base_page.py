from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import base_locators as loc
from utils.wait_utils import wait_for_element_clickable, wait_for_element_to_disappear


class BasePage:
    base_url = "https://www.onliner.by"
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened for this page class')

    def find(self, locator: tuple[str, str]):
        return self.driver.find_element(*locator)

    def find_in_element(self, element: WebElement, locator: tuple[str, str]):
        return element.find_element(*locator)

    def accept_cookie_consent(self):
        wait_for_element_clickable(self.driver, loc.consent_app_popup_loc)
        cookie_accept_button = self.find(loc.cookies_accept_loc)
        cookie_accept_button.click()
        wait_for_element_to_disappear(self.driver, loc.consent_app_popup_loc)

    def get_current_url(self):
        return self.driver.current_url
