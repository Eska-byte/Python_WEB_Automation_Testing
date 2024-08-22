import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helper.config import *


@pytest.fixture()
def open_driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-allow-origins=*")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-web-security")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver

@pytest.fixture(scope='function', autouse=True)
def hook(request, open_driver):
    open_driver.get(web_url)

    yield
    time.sleep(3)
    open_driver.close()
    open_driver.quit()

@pytest.fixture(scope='session', autouse=True)
def suite(request):
    print("\nBefore All")
    yield
    print("\nAfter All")