import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright

# pytest --slowmo 2000 --headed test_dos.py

def test_checkbox4(playwright: Playwright) -> None:
 browser= playwright.chromium.launch(headless=False, slow_mo=400)
 #context= browser.new_context()
 
 context=browser.new_context(viewport={'width':1500, 'height':800})
 
 
 #context=browser.new_context(record_video_dir="Videos/Checkbox")
 page=context.new_page()
 page.goto("https://datatables.net/extensions/select/examples/initialisation/checkbox")
 expect(page).to_have_title("DataTables example - Checkbox selection")
    
    #Tiempo de espera
 page.set_default_timeout(5000)
 
 
 page.mouse.wheel(0,400)
 time.sleep(2)
 
 for i in range (1,11): # el ultimo numero es para incrementar
    page.locator(f"(//td[contains(@class,'  select-checkbox')])[{i}]").click()
    if i==3:
       page.locator("//a[@class='paginate_button '][contains(.,'2')]").click()
       
    if i==6:
       page.locator("//a[contains(@data-dt-idx,'3')]").click()
       page.locator("//input[contains(@type,'search')]").fill("Gloria")
       page.locator("(//td[contains(@class,'  select-checkbox')])[1]").click()
       
       
       
       
    time.sleep(0.7)
 
 