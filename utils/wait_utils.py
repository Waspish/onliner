from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_element_clickable(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


def wait_for_element_to_disappear(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located(locator))
