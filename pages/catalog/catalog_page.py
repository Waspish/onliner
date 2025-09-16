from pages.base.base_page import BasePage
from pages.catalog.locators import catalog_locators as loc
from utils.wait_utils import wait_for_element_clickable


class CatalogPage(BasePage):
    base_url = 'https://catalog.onliner.by'
    page_url = '/'

    def fill_search_field(self, text):
        search_field_element = wait_for_element_clickable(self.driver, loc.search_field_loc)
        search_field_element.click()
        search_field_element.send_keys(text)

    def navigate_to_specific_product_page(self, product_number):
        specific_product_locator = loc.product_element_loc(product_number)
        product_element = wait_for_element_clickable(self.driver, specific_product_locator)
        product_title_element = self.find_in_element(product_element, loc.product_title_loc)
        product_title_text = product_title_element.text
        product_title_link = product_title_element.get_attribute('href')
        product_element.click()
        return product_title_text, product_title_link
