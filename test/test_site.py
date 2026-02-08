
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from pages.homepage import HomePage
from pages.product import ProductPage

# @pytest.fixture
# def driver():
#     browser=webdriver.Chrome()
#     # browser.maximized_window()
#     yield browser
    
def test_open_s6(browser):

    homepage=HomePage(browser)
    homepage.open()
    homepage.click_galaxy_x6()
    product_page=ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')


# Змініть тут 'browser' на 'driver'
def test_open_s6(driver): 
    driver.get('https://demoblaze.com/')
    # Переконайтеся, що тут теж 'driver' і немає друкарських помилок
    galaxy_s6 = driver.find_element(By.LINK_TEXT, "Samsung galaxy s6")
    galaxy_s6.click()


def test_two_monitors(driver):
    homepage=HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    time.sleep(3)
    homepage.check_products_count(2)
    
    
    
    
    
    
    # driver.get('https://demoblaze.com/')
    # monitor=driver.find_element (By.CSS_SELECTOR , '[onclick="byCat(\'monitor\')"]')
    # monitor.click()
    
    # monitors=driver.find_elements(By.CSS_SELECTOR, '.card')
    # assert len(monitors)==2
    
    