# Import the necessary libraries
import ipapi
import json
import msvcrt
import names
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
import pyautogui as gui
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

def create_account(driver: webdriver, is_mobile: bool = False, email: str = None, password: str = None):
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

    # Click first checkbox
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,\
	'/html/body/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div'))).click()
	
    # Wait a few seconds
    time.sleep(randint(5, 10))
    
    # Click second checkbox
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,\
	'/html/body/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div'))).click()
    print("Checkboxes clicked")

    # Click Ok
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,\
	'/html/body/div/div[2]/div[2]/div/div/div/div[3]/button[2]/div'))).click()

    # Wait for the next page to load
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]')))

    # Enter email
    try:
        time.sleep(randint(5, 10))
        gui.press("tab")
        time.sleep(randint(5, 10))
        gui.press("tab")
        gui.typewrite(email)
        print(f"Email: {email}")
    except Exception as e:
        print(e)
        print("Failed to enter email")

    # Wait a few seconds
    time.sleep(randint(5, 10))

    # Enter password
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,\
	    '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/input'))).send_keys(password)
        print(f"Password: {password}")
    except:
        gui.press("tab")
        gui.typewrite(password)
        print(f"Password: {password}")
	
    # Wait a few seconds
    time.sleep(randint(5, 10))
    
    # Accept terms and conditions
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[3]/div/input').click()
    print("Terms and conditions accepted")

    # Wait a few seconds
    time.sleep(randint(5, 10))
    
    # Click age checkbox
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[4]/div/input').click()
    print("Age checkbox clicked")

    # Click Next
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[5]/button/div').click()
    print("Next clicked")

    # Complete the captcha
    # Wait until the 'Enter' key is pressed
    while True:
        if msvcrt.getch() == b'\r':
            print("Captcha completed and account created")
            break


def generate_credentials(i):
    """Generate email and random password."""
    # Shuffling the characters.
    random.shuffle(characters)

    #Picking random characters from the list.
    password = []
    for i in range(10):
        password.append(random.choice(characters))

    # Shuffling the resultant password.
    random.shuffle(password)

    # Converting the list to string.
    password = ("".join(password))

    email = ("XCloud" + generate_username() + "2023")

    return email, password



def generate_username():
    """Generate an username containing the month"""
    # Define a list of the months of the year
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # Return the current month
    return months[i]


def main():
    """Main function."""
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
    
    # Declare global variables
    global i

    # Loop through the months
    for i in range(12):

        # Rotate VPN
        rotate_VPN()
        try:
            # Get current IP address
            check_ip()
        except Exception:
            print("An unexpected error occurred while checking IP address")

        # Generate credentials
        email, password = generate_credentials(i)

        try:
            # Create account
            create_account(driver, location["country_code"] == "US", email, password)
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
        except Exception as e:
            print(e)

        # Terminate NordVPN
        nordvpn_switcher.terminate_VPN()

        # Wait 5 minutes
        time.sleep(300)

        # Increment i
        i += 1

if __name__ == "__main__":
    main()


