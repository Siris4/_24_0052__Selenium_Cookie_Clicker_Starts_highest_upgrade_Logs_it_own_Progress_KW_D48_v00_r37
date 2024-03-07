from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_chrome_driver_for_selenium():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    return driver

def select_language(driver):
    time.sleep(5)  # allows the game to load
    language_selection = driver.find_element(By.ID, "langSelect-EN")
    language_selection.click()
    time.sleep(2)  # waits for language selection to apply

def click_cookie(driver, clicks=200):
    cookie = driver.find_element(By.ID, "bigCookie")
    for _ in range(clicks):
        cookie.click()

def try_clicking_upgrades(driver, upgrade_IDs):
    clicked_successfully = False  # adds a flag to indicate successful click
    for i in range(19, -1, -1):  # adjusts if you have more or fewer products
        if clicked_successfully:
            break  # exits the loop if an upgrade has been successfully clicked
        product_id = f"productName{i}"
        try:
            upgrade_click = driver.find_element(By.ID, product_id)
            if upgrade_click.is_displayed() and upgrade_click.is_enabled():
                while True:
                    try:
                        upgrade_click.click()
                        print(f"Clicked on the upgrade with ID: {product_id}. Trying again if possible.")
                        clicked_successfully = True  # updates the flag after a successful click
                        time.sleep(0.5)  # a brief pause after a successful click
                        # this might need adjustments
                    except ElementClickInterceptedException:
                        print(f"Finished clicking or unable to click more on {product_id}.")
                        break
            else:
                print(f"Upgrade: {product_id} is not clickable due to not being displayed or enabled.")
        except NoSuchElementException:
            print(f"Upgrade with ID: {product_id} does not exist.")
        if clicked_successfully:
            break  # ensures the loop exits if an upgrade has been clicked



# Define your upgrade_IDs dictionary here according to the format provided:
upgrade_IDs = {
    'YOU_UPGRADE': 'productName19',
    'CORTEX_BAKER': 'productName18',
    'IDLEVERSE': 'productName17',
    'JAVASCRIPT_CONSOLE': 'productName16',
    'FRACTAL_ENGINE': 'productName15',
    'CHANCEMAKER': 'productName14',
    'PRISM': 'productName13',
    'ANTIMATTER_CONDENSER': 'productName12',
    'TIME_MACHINE': 'productName11',
    'PORTAL': 'productName10',
    'ALCHEMY_LAB': 'productName9',
    'SHIPMENT': 'productName8',
    'WIZARD_TOWER': 'productName7',
    'TEMPLE': 'productName6',
    'BANK': 'productName5',
    'FACTORY': 'productName4',
    'MINE': 'productName3',
    'FARM': 'productName2',
    'GRANDMA': 'productName1',
    'CURSOR': 'productName0',
}

driver = setup_chrome_driver_for_selenium()
select_language(driver)

# the main loop
while True:
    click_cookie(driver)  # continuously clicks the cookie
    try_clicking_upgrades(driver, upgrade_IDs)  # attempts to click upgrades as described
    time.sleep(5)  # adjust as needed to balance upgrade attempts and cookie clicking
