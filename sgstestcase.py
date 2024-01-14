###############################################################
# * Ariadna Álvarez Navarro * #
# * 14-01-2024 * #
# * Python code for Web Scrapping SGS page with selenium * #
###############################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import pyautogui
import keyboard


# Configure logging
logging.basicConfig(filename='webdriver_log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Create an instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Set up WebDriverWait to wait for elements to load
WDwait = WebDriverWait(driver, 10)

# Maximise the browser window so it fills the entire screen when open
driver.maximize_window()

# Website we want to access
website = 'https://www.sgs.com'


try:
    # Open the URL of the website
    driver.get(website)
    
except Exception as e:
    # If error make a screenshot and close driver
    driver.get_screenshot_as_file('WebsiteError.png')
    logging.error(f"Error trying to reach {website} : {e}")
    driver.quit()

# Wait for 2 seconds
time.sleep(2)


try:
    # Handle cookies pop-up
    error = 'Cookies'
    # Wait for the cookie pop-up to appear
    WDwait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-button-group"]'))
        )

    # Click on "Reject All" button
    WDwait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-reject-all-handler"]'))
        ).click()
    
    # Wait for 2 seconds
    time.sleep(2)

    # Click on "Our Services" in the navigation menu
    error = 'Our Services'
    WDwait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/header/div[2]/div/div[1]/div/ul/li[1]/button'))
        ).click()

    # Wait for 2 seconds
    time.sleep(2)

    # Click on "Health Science" in the dropdown menu
    error = 'Health Science'
    WDwait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/header/div[3]/div/ul/li[2]/ul/li[1]/a'))
        ).click()

    # Wait for 2 seconds
    time.sleep(2)

    # Scroll down the page
    driver.execute_script("window.scrollTo(0, 1600);")

    # Wait for 2 seconds
    time.sleep(2)

    # Click on "Clinical Research" link
    error = 'Clinical Research'
    WDwait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[5]/div/div/div/div/div/div/div/div/div/a[3]/img'))
        ).click()

    # Wait for 2 seconds
    time.sleep(2)

    # Scroll down the page
    driver.execute_script("window.scrollTo(0, 1200);")

    # Wait for 2 seconds
    time.sleep(2)

    # Click on "Biometrics" link
    error = 'Biometrics'
    WDwait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[5]/div/div/div/div/div/div/div/div/div/a[1]/img'))
        ).click()

    # Wait for 2 seconds
    time.sleep(2)

    # Scroll down the page
    driver.execute_script("window.scrollTo(0, 3400);")

    # Wait for 2 seconds
    time.sleep(2)

    # Click on the PDF link
    error = 'PDF link'
    WDwait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[8]/div/div/div[2]/a/div'))
        ).click()

    # Wait for 2 seconds
    time.sleep(2)

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[1])

    # Wait for the PDF page to load
    WDwait.until(EC.presence_of_element_located((By.XPATH, '//body')))

    # Simulate key combination to save the PDF (Cmd + S)
    error = 'Downloading PDF'
    keyboard.press_and_release('command+s')

    # Wait for the save dialog to show
    time.sleep(2)

    # Enter the file name and press Enter to save
    pyautogui.write('SGS_testcase')
    pyautogui.press('enter')

    # Close the PDF tab
    driver.close()

    # Switch back to the main window
    driver.switch_to.window(driver.window_handles[0])

    # Wait for 2 seconds
    time.sleep(2)

    # Scroll up the page
    driver.execute_script("window.scrollTo(0, 0);")

    # Wait for 2 seconds
    time.sleep(2)
    
    # Take a screenshot
    driver.get_screenshot_as_file('screenshotBiometrics.png')
    
except Exception as e:
    # If error make a screenshot and close driver
    driver.get_screenshot_as_file(f'{error}Error.png')
    logging.error(f"Error trying to reach {error} site: {e}")
    driver.quit()

# Wait for 5 seconds
time.sleep(5)

# Close the browser when finished
driver.quit()
