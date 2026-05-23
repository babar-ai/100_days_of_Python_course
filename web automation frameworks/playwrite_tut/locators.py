
import time 
from playwright.sync_api import sync_playwright                        # sync_api provides the synchronous version of Playwright


def run_playwright(url):

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=False)

        page = browser.new_page(viewport={"width": 1280, "height": 720})
        page.goto(url, wait_until="load")
        
        # Locate elements by role
        page.get_by_placeholder("Username").fill("your_username")  # Replace with actual username
        page.get_by_placeholder("Password").fill("your_password")  # Replace with actual password

        time.sleep(5)
        page.close()





url = "https://nrel.eskilled.com.au/login/index.php?loginredirect=1"
run_playwright(url)
