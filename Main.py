from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Define the path to your ChromeDriver executable
chromedriver_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'

# Configure ChromeOptions
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")

# Create a new Service object and pass the path of the ChromeDriver executable to the executable_path attribute
service = Service(chromedriver_path)

# Create a new ChromeDriver object and pass the Service object to the service attribute
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the mobile.de search page
driver.get('https://suchen.mobile.de/fahrzeuge/search.html')

# Wait for the cookie consent popup to appear and click the "Accept All Cookies" button
cookie_consent_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body[@class='has-sticky-bottom-chips']/div[@id='mde-consent-modal-container']/div[@class='sc-iBkjds frmJSB']/div[@class='sc-papXJ ixHhna']/div[@class='sc-jqUVSM dBIrCF']/button[@class='sc-bczRLJ iBneUr mde-consent-accept-btn']")))
cookie_consent_btn.click()

print("Starting")
sleep(1)
print(".")
sleep(1)
print(".")
sleep(1)
print(".")
sleep(1)
print(".")
sleep(1)
print(".")

# Get the user input for the make of the car they want to search for
make = input("Which make would you like to search for? (Mercedes/BMW): ")

# Select the make on the website depending on the user input
if make.lower() == "mercedes":
    make_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'selectMake1-ds')))
    make_input.click()
    make_option = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(), 'Mercedes-Benz')]")))
    make_option.click()
elif make.lower() == "bmw":
    make_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'selectMake1-ds')))
    make_input.click()
    make_option = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(), 'BMW')]")))
    make_option.click()
else:
    print("Invalid make selection")

body_type = input("Which body type would you like to search for? (Coupe/Sedan/Both): ")

if body_type.lower() == "coupe":
    coupe_checkbox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='categories-SportsCar-ds']")))
    actions = ActionChains(driver)
    actions.move_to_element(coupe_checkbox).click().perform()
elif body_type.lower() == "sedan":
    sedan_checkbox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='categories-Limousine-ds']")))
    actions = ActionChains(driver)
    actions.move_to_element(sedan_checkbox).click().perform()
elif body_type.lower() == "both":
    coupe_checkbox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='categories-SportsCar-ds']")))
    sedan_checkbox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='categories-Limousine-ds']")))
    actions = ActionChains(driver)
    actions.move_to_element(coupe_checkbox).click().move_to_element(sedan_checkbox).click().perform()
else:
    print("Invalid body type selection")

# scroll down to make KM and price visible
action = ActionChains(driver)
action.send_keys(Keys.PAGE_DOWN).perform()

# Get the user input for the maximum number of kilometers
while True:
    km_input = input("Enter the maximum number of kilometers (between 0 and 500000): ")
    if km_input.isdigit() and 0 <= int(km_input) <= 500000:
        break
    else:
        print("Invalid input. Please enter a number between 0 and 500000.")

# Enter the maximum number of kilometers into the input box
km_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='maxMileage']")))
km_box.clear()
km_box.send_keys(km_input)
km_box.send_keys(Keys.RETURN)

# Wait for 1 second to ensure the element is fully loaded
sleep(1)

# Get the user input for the maximum price
while True:
    price_input = input("Enter the maximum price (in Euros): ")
    if price_input.isdigit():
        break
    else:
        print("Invalid input. Please enter a number.")

# Enter the maximum price into the input box
max_price = driver.find_element(By.XPATH, "//input[@data-testid='price-max-input']")
max_price.click()
max_price.send_keys(price_input)

# Wait for 1 second to ensure the element is fully loaded
sleep(1)

# Find the search button
search_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "dsp-upper-search-btn")))

# Click the search button
search_button.click()

sleep(5)

# Wait for user input before quitting the browser
input("Press Enter to quit")

# Close the browser window
driver.quit()
