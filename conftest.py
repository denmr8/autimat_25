from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options=Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(3)
    yield browser
    browser.quit()
