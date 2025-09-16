def test_search_product_and_verify_navigation(home_page, catalog_page, product_details_page):
    # variable that stores number of the product to check
    product_number = 3
    home_page.open_page()
    # don't need accept_cookie_consent() in headless mode
    # home_page.accept_cookie_consent()
    home_page.go_to_catalog()
    catalog_page.fill_search_field('iphone')
    # getting product title and product link after search
    product_title, product_link = catalog_page.navigate_to_specific_product_page(product_number)
    # verifying product title and link are the same as were in search results
    product_details_page.check_title_link(product_title, product_link)
