import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ...existing code...
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# ...existing code...
# Initialize the Chrome driver
# We use ChromeDriverManager to automatically handle the correct driver version
print("Starting Chrome browser...")
driver = webdriver.Chrome(ChromeDriverManager().install())
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# ...existing code...


# --- Configuration ---
# IMPORTANT: Replace these placeholders with your actual credentials
USERNAME = "darae1025@hotmail.com" # Placeholder, replace with your actual username
PASSWORD = "4005Qvdarae+" # Placeholder, replace with your actual password
LOGIN_URL = "https://nrel-au.assessapp.com/users/sign_in" 
COURSE_NAME = "Victoria Agents' Representative Course v2"
ASSESSMENT_NAME = "Pre-Enrolment Assessment (Part 1)"


def automate_enrollment_task():
    # Initialize the Chrome driver
    # We use ChromeDriverManager to automatically handle the correct driver version
    print("Starting Chrome browser...")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    
    try:
        # 1. Navigate to the login page
        print(f"Navigating to login page: {LOGIN_URL}")
        driver.get(LOGIN_URL)
        
        # Wait for the email field to be present
        wait = WebDriverWait(driver, 20)
        email_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email ']")))
        password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        sign_in_button = driver.find_element(By.XPATH, "//input[@value='Sign In']")

        # 2. Input username and password and click Sign In
        print("Entering credentials and signing in...")
        email_field.send_keys(USERNAME)
        password_field.send_keys(PASSWORD)
        sign_in_button.click()

        # 3. Wait for the dashboard/main page to load and click 'Enrolments'
        # The URL changes to something like https://au-lrn.assessapp.com/sdawui/dashboard
        print("Waiting for successful login and dashboard load...")
        enrolments_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Enrolments']")))
        enrolments_link.click()
        
        # 4. Wait for the enrolments page to load and click 'Overview' for the specific course
        print(f"Navigating to the overview of the course: '{COURSE_NAME}'")
        # Find the course container
        course_xpath = f"//div[contains(text(), \"{COURSE_NAME}\")]/ancestor::div[contains(@class, 'card')]"
        course_container = wait.until(EC.presence_of_element_located((By.XPATH, course_xpath)))
        
        # Find the 'Overview' button within that course container
        overview_button = course_container.find_element(By.XPATH, ".//a[text()='Overview']")
        overview_button.click()

        # 5. Wait for the course journey page to load and click the 'Pre-Enrolment Assessment' stage
        print("Entering the 'Pre-Enrolment Assessment' stage...")
        # The stage is a div with a button to expand it
        pre_enrolment_stage_xpath = "//div[contains(text(), 'Pre-Enrolment Assessment')]/ancestor::div[contains(@class, 'stage-header')]/following-sibling::button"
        pre_enrolment_stage_button = wait.until(EC.element_to_be_clickable((By.XPATH, pre_enrolment_stage_xpath)))
        pre_enrolment_stage_button.click()
        
        # Wait for the activities to appear and click the first one
        print(f"Clicking on the first assessment task: '{ASSESSMENT_NAME}'")
        assessment_link_xpath = f"//div[contains(text(), \"{ASSESSMENT_NAME}\")]/ancestor::a"
        assessment_link = wait.until(EC.element_to_be_clickable((By.XPATH, assessment_link_xpath)))
        assessment_link.click()
        
        # 6. Wait for the assessment page to load and click 'Save'
        print("Waiting for assessment page to load and clicking 'Save'...")
        # The save button is an input with value 'Save'
        save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Save']")))
        save_button.click()
        
        print("Successfully completed all steps: Logged in, navigated to course, entered assessment, and clicked Save.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        # Optionally, save a screenshot on error
        driver.save_screenshot("error_screenshot.png")
        print("Screenshot saved as error_screenshot.png")
        
    finally:
        # Close the browser
        print("Closing browser in 5 seconds...")
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    automate_enrollment_task()


