import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from Funciones import Funciones_Globales

# primero correr de formar normal y despues ejecutar el comando(playwright show-trace trace.zip)
# playwright show-trace trace.zip

pdf1="C:/Users/rodri/Videos/Playwrite/Curso/Estudiantes/Ejemplos/PDF/dgmn-certificado-de-situacion-militar-17276128.pdf"

def test_Upload(playwright: Playwright) -> None:
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
 F.Texto("//input[contains(@id,'firstName')]","Rodrigo",1)
 F.Texto("//input[contains(@id,'lastName')]","Vizama",1)
 F.Texto("//input[contains(@id,'userEmail')]","rodrigo.vizama@gmail.com",1)


#seleccion
 F.Click("//label[@for='gender-radio-1'][contains(.,'Male')]",1)
 
 F.Texto("//input[contains(@id,'userNumber')]","984862714",1)
 
 #Calendarios
 #F.Click("#dateOfBirthInput","21 Feb 2024",tiempo=0.5)
 #Segunda forma
 F.Click("//input[contains(@id,'dateOfBirthInput')]",tiempo=0.5)
 F.Click("//input[contains(@value,'23 Feb 2024')]",tiempo=0.5)
 
 #Subir archivos
 F.Upload_File("//input[contains(@type,'file')]",pdf1,tiempo=1)
 
 #Remove File
 
 F.Upload_File_remove("//input[contains(@type,'file')]",tiempo=1)
 
 F.Upload_File("//input[contains(@type,'file')]",pdf1,tiempo=1)
 
 
 #page.mouse.click(0,50)
 #page.locator("#dateOfBirthInput").click()
 #page.get_by_label("Choose Wednesday, February 21st,").click()
 
 #Funcion para dar click al teclado en la opcion tab
 #page.keyboard.press("Tab")
 #Combobox
 page.wait_for_load_state()
 page.click('//div[@id=\'state\']//div[contains(@class,\'css-1wy0on6\')]')
 time.sleep(2)
 page.get_by_text("NCR", exact=True).click()
 #page.get_by_text('NCR')
 time.sleep(2)
 
 page.click("//div[@class=' css-1hwfws3'][contains(.,'Select City')]")
 time.sleep(2)
 page.get_by_text("Gurgaon", exact=True).click()
 time.sleep(2)
 #Combobox
 #F.combo_value("//div[@id=\'state\']//div[contains(@class,\'css-1wy0on6\')]","Uttar Pradesh",1)
 #page.getByLabel('//div[@id=\'state\']//div[contains(@class,\'css-1wy0on6\')]').selectOption('NCR')
 #page.getByLabel("//div[@class=' css-1wa3eu0-placeholder'][contains(.,'Select State')]").selectOption({label: 'NCR' })


#Cierre de trace viewer

 context.tracing.stop(path="trace.zip")
 context.close()
 browser.close()
