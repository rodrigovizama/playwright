import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from Funciones import Funciones_Globales

#playwright codegen https://www.saucedemo.com/

# primero correr de formar normal y despues ejecutar el comando(playwright show-trace trace.zip)
# playwright show-trace trace.zip

#Lanzando el debug
#set PWDEBUG=1
# salir del modo debug PWDEBUG=0
#pytest Debug.py -S

pdf1="C:/Users/rodri/Videos/Playwrite/Curso/Estudiantes/Ejemplos/PDF/dgmn-certificado-de-situacion-militar-17276128.pdf"

def test_Generate(playwright: Playwright) -> None:
 browser= playwright.chromium.launch(headless=False, slow_mo=400)
 context= browser.new_context()
 context=browser.new_context(viewport={'width':1500, 'height':800})
 page=context.new_page()
 page.goto("https://demoqa.com/automation-practice-form")
 expect(page).to_have_title("DEMOQA")
 
 #Inicia Trace Viewe
 context.tracing.start(screenshots=True, snapshots=True,sources=True)
  #grabar playwright codegen https://demoqa.com/automation-practice-form
  #Tiempo de espera
 page.set_default_timeout(5000)
 
 
 
 #Creando nuestro objeto de tipo funciones globales
 F=Funciones_Globales(page)
 #time.sleep(2)
 #page.mouse.wheel(0,400)
 F.Scroll_xy(0,400)
 F.Esperar(1)