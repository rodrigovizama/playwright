import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    
 
    context=browser.new_context(viewport={'width':1500, 'height':800})
 
 
    context=browser.new_context(record_video_dir="Videos/Checkbox")
    page = context.new_page()
    page.goto("https://demoqa.com/checkbox")
    page.get_by_label("Toggle").click()
    page.locator("li").filter(has_text=re.compile(r"^Desktop$")).get_by_label("Toggle").click()
    page.locator("label").filter(has_text="Commands").get_by_role("img").first.click()
    page.locator("li").filter(has_text=re.compile(r"^Documents$")).get_by_label("Toggle").click()
    page.locator("label").filter(has_text="Office").get_by_role("img").first.click()
    page.locator("li").filter(has_text=re.compile(r"^Downloads$")).get_by_label("Toggle").click()
    page.locator("label").filter(has_text="Word File.doc").get_by_role("img").first.click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
