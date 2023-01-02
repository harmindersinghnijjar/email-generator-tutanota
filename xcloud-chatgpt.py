# Import the necessary libraries
import ipapi
import json
import random
import requests
import string
import time

from random  import randint
from nordvpn_switcher import initialize_VPN,rotate_VPN,terminate_VPN
import selenium.common.exceptions as exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import nordvpn_switcher
import pygetwindow as gw

# Characters to generate password from.
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# Define user-agents
PC_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63"
)
MOBILE_USER_AGENT = (
    "Mozilla/5.0 (Linux; Android 10; Pixel 3) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/79.0.3945.79 Mobile Safari/537.36"
)

def check_ip():
    """Check the IP address of the provided webdriver."""
    ip = (json.loads(requests.get("https://ip.seeip.org/jsonip?").text)["ip"])
    print(f"IP: {ip}")

def create_account(driver: webdriver, is_mobile: bool = False):
    """Create a Tutanota email account using the provided webdriver."""
    # Open Tutanota
    url = "https://mail.tutanota.com/signup"
    driver.get(url)

    # Wait for the page to load
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body")))
    print("Page loaded")
    
    # Sleep for a random amount of time
    time.sleep(randint(5, 10))
    print("Sleeping")

    # Click the free option
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[5]/button'))).click()
    print("Free option selected")

    # Wait for the next page to load
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]')))
    print("Page loaded")

    # Click both checkboxes
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,\
	'/html/body/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div'))).click()
	# Wait a few seconds
    time.sleep(randint(2, 4))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,\
	'/html/body/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div'))).click()
    print("Checkboxes clicked")

    # Click Ok
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,\
	'/html/body/div/div[2]/div[2]/div/div/div/div[3]/button[2]/div'))).click()

    # Wait for the next page to load
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]')))

    # Generate a random email address and password
    email = "".join(random.choices(characters, k=10)) + "@tutanota.com"
    password = "".join(random.choices(characters, k=12))

    # Enter email and password
    email_field = driver.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/input'
    )
    email_field.send_keys(email)
    password_field = driver.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div[2]/input'
    )
    password_field.send_keys(password)

    # Click create account
    create_button = driver.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div/div/div/div[3]/button[2]/div'
    )
    create_button.click()

    # Wait for the account creation to complete
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]')))

def main():
    # Initialize NordVPN
    nordvpn_switcher.initialize_VPN(save = 0, area_input=["complete rotation"])

    # Get current location
    try:
        location = json.loads(requests.get("https://ipapi.co/json").text)
        print(location)
    except Exception:
        print("An unexpected error occurred while getting location")

    # Set up webdriver
    options = FirefoxOptions()
    # Set headless to False if you want to see the browser
    options.headless = False
    user_agent = MOBILE_USER_AGENT if location["country_code"] == "US" else PC_USER_AGENT
    options.add_argument(f"user-agent={user_agent}")
    driver = webdriver.Firefox(options=options, service=FirefoxService(executable_path=GeckoDriverManager().install()))
    driver.set_page_load_timeout(30)
    #driver.set_window_size(640, 480)

    for i in range(10):
        rotate_VPN()
        try:
            check_ip()
        except Exception:
            print("An unexpected error occurred while checking IP address")

        try:
            create_account(driver, location["country_code"] == "US")
        except exceptions.TimeoutException:
             print("Timed out while creating account")
        except exceptions.NoSuchElementException:
            print("Unable to find element while creating account")
        except exceptions.ElementNotInteractableException:
            print("Element not interactable while creating account")
        except exceptions.UnexpectedAlertPresentException:
            print("Unexpected alert present while creating account")
        except exceptions.NoAlertPresentException:
            print("No alert present while creating account")
        except Exception:
            print("An unexpected error occurred while creating account")

        # Terminate NordVPN
        nordvpn_switcher.terminate_VPN()

if __name__ == "__main__":
    main()


