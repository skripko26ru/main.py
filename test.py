"""
import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        print("RES: ", response.url)

        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys("webElement")

# Get attribute of current active element
attr = driver.switch_to.active_element.get_attribute("title")
print(attr)

driver.get('https://www.example.com')
# ffffff

cssValue = driver.find_element(By.LINK_TEXT, "More information...").value_of_css_property('color')
print(cssValue)
