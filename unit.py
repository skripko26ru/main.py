import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestSelenium(unittest.TestCase):
    def test_1(self) -> None:
        browser = webdriver.Chrome()
        browser.get('http://tutorialsninja.com/demo')

        field_search = browser.find_element(by=By.NAME, value="search")
        field_search.send_keys("iphone")
        field_search.send_keys(Keys.ENTER)

        button_add = browser.find_element(by=By.XPATH,
                                          value='//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]')
        button_add.click()

        link_shopping_cart = browser.find_element(by=By.XPATH, value='//*[@id="top-links"]/ul/li[4]/a/i')
        link_shopping_cart.click()

        self.assertTrue("product 11" in browser.page_source)
        browser.close()
