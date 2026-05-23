from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys                 # For sending keyboard keys
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

time.sleep(5)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")  # This will raise an exception since the driver hasn't navigated to any page yet
input_element.send_keys("Selenium tutorial" + Keys.ENTER)



time.sleep(5)
driver.quit()