from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

login_current = "20002025"
password_current = "123123Qw!"
func_key = "590"

browser = webdriver.Chrome()
# browser = webdriver.Firefox()

try:
    browser.get('https://ift-ibrb1-sharing.vtb.ru/login')

    # waiting for login page to open
    WebDriverWait(browser, 30).until(
        ec.presence_of_element_located((By.TAG_NAME, "h1"))
    )

    # clicking on login tab
    tab_login = browser.find_element(by=By.XPATH, value='//*[@id="login"]/div[1]')
    tab_login.click()

    # login input
    field_login = browser.find_element(by=By.XPATH,
                                       value='/html/body/div[1]/div[3]/main/div/div/div[1]/div[1]/div/div['
                                             '1]/form/div[2]/div/div/input')
    field_login.send_keys(login_current)
    field_login.send_keys(Keys.ENTER)

    # password entry
    field_password = browser.find_element(by=By.XPATH,
                                          value='/html/body/div[1]/div[3]/main/div/div/div[1]/div[1]/div/div['
                                                '1]/form/div[3]/div/div[1]/input')
    field_password.send_keys(password_current)
    field_password.send_keys(Keys.ENTER)

    # waiting for home page to open
    WebDriverWait(browser, 40).until(
        ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/header/div/div/div[3]/div/div/div['
                                                  '2]/div/section/div[2]/div[2]/div/button'))
    )

    # Close promo banner
    banner_promo = browser.find_element(by=By.XPATH,
                                        value='/html/body/div[1]/div[3]/header/div/div/div[3]/div/div/div['
                                              '2]/div/section/div[2]/div[2]/div/button')
    banner_promo.click()

    # Close promo banner
    icon_profile = browser.find_element(by=By.XPATH,
                                        value='/html/body/div[1]/div[3]/header/div/div/div[2]/button/div[1]')
    icon_profile.click()

    browser.get('https://ift-ibrb1-sharing.vtb.ru/function-settings')

    WebDriverWait(browser, 40).until(
        ec.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[5]/div/div/div/div/div[2]/div[2]/div[2]/div/input'))
    )

    # function input
    field_func = browser.find_element(by=By.XPATH,
                                      value='/html/body/div[1]/div[5]/div/div/div/div/div[2]/div[2]/div[2]/div/input')

    print("FFF", field_func)
    field_func.send_keys(func_key)
    field_func.send_keys(Keys.ENTER)

    toggle_func = browser.find_element(by=By.XPATH,
                                       value='/html/body/div[1]/div[5]/div/div/div/div/div[2]/div[3]/div/div['
                                             '2]/label/span')
    print("TOG", toggle_func)

finally:
    print("EEEww")
    # browser.quit()

'''
browser.get('http://tutorialsninja.com/demo')

field_search = browser.find_element(by=By.NAME, value="search")
field_search.send_keys("iphone")
field_search.send_keys(Keys.ENTER)

button_add = browser.find_element(by=By.XPATH, value='//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]')
button_add.click()

link_shopping_cart = browser.find_element(by=By.XPATH, value='//*[@id="top-links"]/ul/li[4]/a/i')
link_shopping_cart.click()

assert "product 11" in browser.page_source
browser.close()



'''
