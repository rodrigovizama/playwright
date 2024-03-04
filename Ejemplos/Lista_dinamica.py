import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from Funciones import Funciones_Globales

def test_Lista_dinamica(playwright: Playwright) -> None:
 browser= playwright.chromium.launch(headless=False, slow_mo=400)
 context= browser.new_context()
 context=browser.new_context(viewport={'width':1500, 'height':800})
 page=context.new_page()
 page.goto("https://www.google.cl/")
 expect(page).to_have_title("Google")
 F=Funciones_Globales(page)
 page.set_default_timeout(5000)
 F.Scroll_xy(0,400)
 
 F.Texto("//textarea[contains(@id,'APjFqb')]","ronal",1)
 F.Click("//span[contains(.,'Ronaldo')]",1)
 F.Esperar(3)
 
 context.close()
 browser.close()
