import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.catalog.catalog_page import CatalogPage
from pages.catalog.product_details_page import ProductDetailsPage
from pages.main_site.home_page import HomePage
from utils.screenshot import take_screenshot


@pytest.fixture
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_driver = webdriver.Chrome(options=chrome_options)
    yield chrome_driver
    if request.session.testsfailed > 0:
        take_screenshot(chrome_driver, request.node.name)
    chrome_driver.quit()


@pytest.fixture
def home_page(driver):
    yield HomePage(driver)


@pytest.fixture
def catalog_page(driver):
    yield CatalogPage(driver)


@pytest.fixture
def product_details_page(driver):
    yield ProductDetailsPage(driver)
