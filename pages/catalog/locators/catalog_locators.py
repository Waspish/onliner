from selenium.webdriver.common.by import By

search_field_loc = (By.CSS_SELECTOR, '.fast-search__form input')


def product_element_loc(product_number):
    return By.CSS_SELECTOR, f'.search__results > li:nth-child({product_number})'


product_title_loc = (By.CSS_SELECTOR, '.product__title-link')
