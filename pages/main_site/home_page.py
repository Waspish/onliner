from pages.base.base_page import BasePage
from pages.main_site import home_locators as loc


class HomePage(BasePage):
    page_url = '/'

    def go_to_catalog(self):
        catalog_element = self.find(loc.catalog_loc)
        catalog_element.click()
