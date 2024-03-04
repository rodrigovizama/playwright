import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright

# pytest --slowmo 2000 --headed test_dos.py

def test_checkbox(playwright: Playwright) -> None:
 browser= playwright.chromium.launch(headless=False, slow_mo=1000)
 #context= browser.new_context()
 
 context=browser.new_context(viewport={'width':1500, 'height':800})
 
 
 #context=browser.new_context(record_video_dir="Videos/Checkbox")
 page=context.new_page()
 page.goto("https://demoqa.com/checkbox")
 expect(page).to_have_title("DEMOQA")
    
    #Tiempo de espera
 page.set_default_timeout(5000)
 
 #che1=page.locator("//button[contains(@aria-label,'Toggle')]")
 #Primera opcion
 page.locator("//button[contains(@aria-label,'Toggle')]").click()
 #che1=page.locator("(//span[contains(@class,'rct-checkbox')])[1]")
 #expect(che1).to_be_visile()
 #che1.click()
 
 #Segunda opcion
 page.locator("(//button[contains(@aria-label,'Toggle')])[2]").click()
 #Tercera opcion
 page.locator("text=Commands").click()
    
#Cerrar context y navegador
 context.close()
 browser.close()