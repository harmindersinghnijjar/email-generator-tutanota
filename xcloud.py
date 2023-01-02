# Import the necessary libraries
from nordvpn_switcher import initialize_VPN,rotate_VPN,terminate_VPN
from random import randint
from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException, UnexpectedAlertPresentException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import ipapi
import msvcrt
import names
import pyautogui as gui
import pygetwindow as gw
import random
import string
import time

# Characters to generate password from.
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# Define user-agents
PC_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'
MOBILE_USER_AGENT = 'Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0. 3945.79 Mobile Safari/537.36'

# Create Tutanota account
def accountCreation(browser: webdriver, isMobile: bool = False):
    # Open Tutanota
    url = 'https://mail.tutanota.com/signup'

    browser.get(url)
    # Wait a few seconds
    time.sleep(randint(2, 10))
	# Select free option
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,\
	'/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[5]/button/div'))).click()
	# Wait a few seconds
    time.sleep(randint(2, 4))
	# Click both checkboxes
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,\
	'/html/body/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div'))).click()
	# Wait a few seconds
    time.sleep(randint(2, 4))
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,\
	'/html/body/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div'))).click()
	# Wait a few seconds
    time.sleep(randint(2, 4))
	# Click Ok
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,\
	'/html/body/div/div[2]/div[2]/div/div/div/div[3]/button[2]/div'))).click()
    # Wait a few seconds
    time.sleep(randint(10, 20))
    # Tab to the on the username field
    gui.press('tab')
    # Wait a few seconds
    time.sleep(randint(2, 4))
    # Tab to the on the username field
    gui.press('tab')
    # Wait a few seconds
    time.sleep(randint(2, 4))
    # Enter username
    gui.write(username)
	# Wait a few seconds
    time.sleep(randint(10, 20))
    # Enter password
    browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/input').send_keys(password)
	# Wait a few seconds
    time.sleep(randint(10, 20))
	# Accept terms and conditions
    browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[3]/div/input').click()
	# Wait a few seconds
    time.sleep(randint(2, 4))
    browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[4]/div/input').click()
	# Click Next
    browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[5]/button/div').click()
    


# Define browser setup function
def browserSetup(headless_mode: bool = False, user_agent: str = PC_USER_AGENT) -> webdriver:
    # Create Firefox browser
    options = FirefoxOptions()
    options.add_argument("user-agent=" + user_agent)
    options.add_argument('lang=' + LANG.split("-")[0])
    options.add_argument("--incognito")
    if headless_mode :
        options.add_argument("--headless")
    options.add_argument('log-level=3')
    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
    from selenium import webdriver
    option = webdriver.FirefoxOptions()
    option.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    #driver = webdriver.Firefox(firefox_binary=firefox_binary)
    driver = webdriver.Firefox(options=option)
    #driver = webdriver.Firefox(executable_path = r'C:\Users\15099\.wdm\drivers\geckodriver\win64\0.32\geckodriver.exe')  
    return driver

def generate_username():
    # define a list of the months of the year
    months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
    # return the current month
    return months[i]




# Generate random credentials
def generate_credentials(i):
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
    firstName = names.get_first_name(gender = 'male')
    lastName = names.get_last_name()
    trailing_digits = randint(1000, 10000)
    trailing_digits = str(trailing_digits)

    username = ("XCloud" + generate_username() + "2023")

    return firstName, lastName, username, password

# Define CCodeLangAndOffset function
def getCCodeLangAndOffset() -> tuple:
    try:
        nfo = ipapi.location()
        lang = nfo['languages'].split(',')[0]
        geo = nfo['country'] 
        tz = str(round(int(nfo['utc_offset']) / 100 * 60))
        return(lang, geo, tz)
    except:
        return('en-EN', 'En', '120')

# Define ipCheck function
def ipCheck(browser: webdriver, isMobile: bool = False):
    # Access to IP Burger
    browser.get('https://ipburger.com')
    # Wait complete loading
    waitUntilVisible(browser, By.ID, 'ipaddress1', 10)
    # Extract IP information
    ip = browser.find_element(By.ID, 'ipaddress1').get_attribute("innerHTML")
    country = browser.find_element(By.ID, 'country_fullname').get_attribute("textContent")
    location = browser.find_element(By.ID, 'location').get_attribute("textContent")
    isp = browser.find_element(By.ID, 'isp').get_attribute("textContent")
    host_name = browser.find_element(By.ID, 'hostname').get_attribute("textContent")
    ip_type = browser.find_element(By.ID, 'ip_type').get_attribute("textContent")
    version = browser.find_element(By.ID, 'version').get_attribute("textContent")
    filename = open('credentials','a')
    filename.write('\n')	
    filename.write(ip)
    filename.write(',')	
    filename.write(country)	
    filename.write(',')
    filename.write(location)
    filename.write(',')	
    filename.write(isp)
    filename.write(',')	
    filename.write(host_name)
    filename.write(',')	
    filename.write(ip_type)
    filename.write(',')	
    filename.write(version)
    filename.write(',')
    filename.write(username + '@tutanota.com')
    filename.write(',')
    filename.write(password)
    time.sleep(randint(5,10))
    
    #browser.quit()

# Define waitUntilVisible function
def waitUntilVisible(browser: webdriver, by_: By, selector: str, time_to_wait: int = 10):
    WebDriverWait(browser, time_to_wait).until(ec.visibility_of_element_located((by_, selector)))

# Define waitUntilClickable function
def waitUntilClickable(browser: webdriver, by_: By, selector: str, time_to_wait: int = 10):
    WebDriverWait(browser, time_to_wait).until(ec.element_to_be_clickable((by_, selector)))


# Define main function
def main():
    # Initialize the VPN
    #initialize_VPN(save=1, area_input=['random regions United States 6'])
    # Set the month to July
    i = 6
    # Set the counter to 1
    j = 1
    # Rotate the VPN 12 times
    try:
        for j in range(12):
            #rotate_VPN()
            # Generate credentials for the current month
            firstName, lastName, username, password = generate_credentials(i)
            # Print the credentials
            print(f"{firstName}, {lastName}, {username}, {password}")
            # Get the CCode, Lang and Offset
            LANG, GEO, TZ = getCCodeLangAndOffset()
            # Setup the browser
            browser = browserSetup(False, MOBILE_USER_AGENT)
            # Access to the IPBurger website
            ipCheck(browser)
            # Access to the Tutanota website
            accountCreation(browser)
            # Wait until the 'Enter' key is pressed
            while True:
                if msvcrt.getch() == b'\r':
                    break
            # Close the browser
            browser.quit()
            i = i + 1
    except Exception as e:
        print(e)

# Run the main function
if __name__ == '__main__':
    main()

		





