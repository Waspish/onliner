from pages.catalog.catalog_page import CatalogPage
from pages.catalog.locators.product_details_locators import product_title_loc


class ProductDetailsPage(CatalogPage):

    def check_title_link(self, product_title, product_link):
        product_title_text = self.find(product_title_loc).text
        assert self.get_current_url() == product_link
        assert product_title == product_title_text
