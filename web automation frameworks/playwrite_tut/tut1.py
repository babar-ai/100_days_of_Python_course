# how to load playwright 

import time 
from playwright.sync_api import sync_playwright                        # sync_api provides the synchronous version of Playwright



with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)                            # Launch a Chromium browser instance in non-headless mode and set headless=True to hide the browser window

    page = browser.new_page(viewport={"width": 1280, "height": 720})                                             # Open a new browser page

    page.goto("https://nrel.eskilled.com.au/login/index.php?loginredirect=1", wait_until="load")  # Navigate to the specified URL and wait until the page is fully loaded

    page.screenshot(path="example.png")                                   # Take a screenshot of the page and save it as 'example.png'
    time.sleep(5)                                                        # Wait for 5 seconds to allow manual inspection of the browser
    browser.close()                                                         # Close the browser instance




# to refactor this code to funtion based structure.

def run_playwright(url):

    with sync_playwright() as playwright:

        with playwright.chromium.launch(headless=False) as browser:

            page = browser.new_page(viewport={"width": 1280, "height": 720})
            page.goto(url, wait_until="load")
            page.screenshot(path="test.png")
            time.sleep(5)
            page.close()


url = "https://nrel.eskilled.com.au/login/index.php?loginredirect=1"
run_playwright(url)
