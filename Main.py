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


print("Starting Chromedriver")
# Define the path to your ChromeDriver executable
chromedriver_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'

print("1/6")

# Configure ChromeOptions
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")

print("2/6")

# Create a new Service object and pass the path of the ChromeDriver executable to the executable_path attribute
service = Service(chromedriver_path)

print("3/6")

# Create a new ChromeDriver object and pass the Service object to the service attribute
driver = webdriver.Chrome(service=service, options=options)

print("4/6")

# Navigate to the mobile.de search page
driver.get('https://suchen.mobile.de/fahrzeuge/search.html')

print("5/6")

# Wait for the cookie consent popup to appear and click the "Accept All Cookies" button
cookie_consent_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 "/html/body[@class='has-sticky"
                                                                                 "-bottom-chips']/div["
                                                                                 "@id='mde-consent-modal-container"
                                                                                 "']/div[@class='sc-iBkjds "
                                                                                 "frmJSB']/div[@class='sc-papXJ "
                                                                                 "ixHhna']/div[@class='sc-jqUVSM "
                                                                                 "dBIrCF']/button[@class='sc-bczRLJ "
                                                                                 "iBneUr "
                                                                                 "mde-consent-accept-btn']")))

print("6/6")

cookie_consent_btn.click()


def startup_wait():
    print("Loading Mobile.de")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print("Mobile.de is ready now")


def car_make_selection():
    # Get the user input for the make of the car they want to search for
    make = input("Which make would you like to search for? (Mercedes/BMW): ")

    # Select the make on the website depending on the user input
    if make.lower() == "mercedes":
        make_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'selectMake1-ds')))
        make_input.click()
        make_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//option[contains(text(), 'Mercedes-Benz')]")))
        make_option.click()
    elif make.lower() == "bmw":
        make_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'selectMake1-ds')))
        make_input.click()
        make_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//option[contains(text(), 'BMW')]")))
        make_option.click()
    else:
        print("Invalid make selection")


def body_type_selection():
    body_type = input("Which body type would you like to search for? (Coupe/Sedan/Both): ")

    if body_type.lower() == "coupe":
        coupe_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='categories-SportsCar-ds']")))
        actions = ActionChains(driver)
        actions.move_to_element(coupe_checkbox).click().perform()
    elif body_type.lower() == "sedan":
        sedan_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='categories-Limousine-ds']")))
        actions = ActionChains(driver)
        actions.move_to_element(sedan_checkbox).click().perform()
    elif body_type.lower() == "both":
        coupe_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='categories-SportsCar-ds']")))
        sedan_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='categories-Limousine-ds']")))
        actions = ActionChains(driver)
        actions.move_to_element(coupe_checkbox).click().move_to_element(sedan_checkbox).click().perform()
    else:
        print("Invalid body type selection")


def max_kilometers_selection():
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


def reg_year_selection():
    # Get the user input for the maximum year of registration
    while True:
        registration_input = input("Enter the newest year of registration you want: ")
        if registration_input.isdigit():
            break
        else:
            print("Invalid input. Please enter a number.")

    # Enter the registration year into the input box
    max_registration = driver.find_element(By.ID, "maxFirstRegistrationDate")
    max_registration.click()
    max_registration.send_keys(registration_input)


def max_price_selection():
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


def location_selection():
    # Get the user input for his zip code
    while True:
        zipcode_input = input("Enter your zip code: ")
        if zipcode_input.isdigit():
            break
        else:
            print("Invalid input. Please enter a number.")

    # Enter the zip code into the input box
    zipcode = driver.find_element(By.ID, "ambit-search-location")
    zipcode.click()
    zipcode.send_keys(zipcode_input)
    zipcode.send_keys(Keys.RETURN)


def radius_selection():
    # Get the user input for the search radius
    while True:
        radius_input = input("Enter your desired search radius in Km: ")
        if radius_input.isdigit():
            break
        else:
            print("Invalid input. Please enter a number.")

    # Enter the zip code into the input box
    radius = driver.find_element(By.ID, "ambit-search-radius")
    radius.click()
    radius.send_keys(radius_input)


# waits so the page gets loaded correctly
startup_wait()

car_make_selection()

# Wait for 1 second to ensure the element is fully loaded
sleep(1)

body_type_selection()

# Wait for 1 second to ensure the element is fully loaded
sleep(1)

driver.execute_script("window.scrollTo(0, 1000)")

max_kilometers_selection()

# Wait for 1 second to ensure the element is fully loaded
sleep(1)

reg_year_selection()

# Wait for 1 second to ensure the element is fully loaded
sleep(1)

max_price_selection()

# Wait for 1 second to ensure the element is fully loaded
sleep(1)

location_selection()

# Wait for 1 second to ensure the element is fully loaded
sleep(1)

radius_selection()

# Wait for 1 second to ensure the element is fully loaded
sleep(1)

# Find the search button
search_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "dsp-upper-search-btn")))

# Click the search button
search_button.click()

startup_wait()

result_list_headline = driver.find_element(By.XPATH, "//h1[@data-testid='result-list-headline']")
results = result_list_headline.text
print("".join(filter(str.isdigit, results)), "Results")

# Wait for user input before quitting the browser
input("Press Enter to quit")

# Close the browser window
driver.quit()
