import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.catalog.catalog_page import CatalogPage
from pages.catalog.product_details_page import ProductDetailsPage
from pages.main_site.home_page import HomePage


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument('headless')
    chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver.set_window_size(1024, 768)
    yield chrome_driver
    if request.node.rep_call.failed:
        take_screenshot(chrome_driver, request.node.name)


@pytest.fixture
def home_page(driver):
    yield HomePage(driver)


@pytest.fixture
def catalog_page(driver):
    yield CatalogPage(driver)


@pytest.fixture
def product_details_page(driver):
    yield ProductDetailsPage(driver)


def take_screenshot(driver, test_name):
    try:
        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/{test_name}_{timestamp}.png"
        driver.save_screenshot(filename)
        print(f"Screenshot: {filename}")
    except Exception as e:
        print(f"Screenshot failed: {e}")
