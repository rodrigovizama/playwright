import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright

# pytest --slowmo 2000 --headed test_dos.py
#def test_dos(page: Page):
def test_dos(playwright: Playwright) -> None:
 browser= playwright.chromium.launch(headless=False, slow_mo=1000)
 #context= browser.new_context()
 
 context=browser.new_context(viewport={'width':1500, 'height':800})
 
 
 #context=browser.new_context(record_video_dir="Videos/Input")
 page=context.new_page()
 page.goto("https://demoqa.com/")
 expect(page).to_have_title("DEMOQA")
    
    #Tiempo de espera
 page.set_default_timeout(5000)
    
    #boton uno
    #boton_uno=page.locator("text=Elements")
 page.locator("text=Elements").click()
 page.screenshot(path="imagenes/boton_uno_click.png")
    #boton_uno.click()
    #page.screenshot(path="imagenes/boton_click.png")
    
    # Validar url
 expect(page).to_have_url(re.compile(".*elements"))
    
 page.locator("text=Text Box").click()
 page.screenshot(path="imagenes/boton_dos_click.png")
 expect(page).to_have_url(re.compile(".*text-box"))
    
    #Primer texto campo nombre
    
 page.locator("#userName").fill("Rodrigo")
 page.screenshot(path="imagenes/texto_nombre_.png")
    #Tiempo forzado
 time.sleep(5)
    
 page.locator("#userEmail").fill("rodrigo@gmail.com")
 page.screenshot(path="imagenes/texto_email_.png")
    
 page.locator("#currentAddress").fill("Direccion 1")
 page.screenshot(path="imagenes/texto_direccion1_.png")
    
 page.locator("#permanentAddress").fill("Direccion 2")
 page.screenshot(path="imagenes/texto_direccion2_.png")
    
 page.locator("text=submit").click()
 page.screenshot(path="imagenes/boton_tres_click.png")
 
 #Cerrar context y navegador
 context.close()
 browser.close()
    
    