import re
import time
import random
import pytest
import sys
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from Funciones import Funciones_Globales

#url="https://www.saucedemo.com/"
url="https://demoqa.com/automation-practice-form"


pdf1="C:/Users/rodri/Videos/Playwrite/Curso/Estudiantes/Ejemplos/PDF/dgmn-certificado-de-situacion-militar-17276128.pdf"
@pytest.fixture(scope="session")
def set_up(playwright: Playwright) -> None:
 browser= playwright.chromium.launch(headless=False, slow_mo=400)
 context= browser.new_context()
 context=browser.new_context(viewport={'width':1500, 'height':800})
 page=context.new_page()
 page.goto(url)
 expect(page).to_have_title("Swag Labs")
 F=Funciones_Globales(page)
 
 #Inicia Trace Viewe
 context.tracing.start(screenshots=True, snapshots=True,sources=True)
 page.set_default_timeout(5000)
 F.Click("//input[contains(@id,'user-name')]",1)
 F.Texto("//input[contains(@id,'user-name')]","standard_user",1)
 F.Click("//input[contains(@id,'password')]",1)
 F.Texto("//input[contains(@id,'password')]","secret_sauce",1)
 F.Click("//input[contains(@id,'login-button')]",1)
 yield page
 context.close()
 browser.close()

@pytest.fixture(scope="function")
def set_up_parametrizar(playwright: Playwright) -> None:
 browser= playwright.chromium.launch(headless=False, slow_mo=400)
 context= browser.new_context()
 context=browser.new_context(viewport={'width':1500, 'height':800})
 page=context.new_page()
 url="https://demoqa.com/automation-practice-form"
 page.goto(url)
 expect(page).to_have_title("DEMOQA")
 F=Funciones_Globales(page)
 context.tracing.start(screenshots=True, snapshots=True,sources=True)
 context.tracing.stop(path="trace.zip")
 page.set_default_timeout(5000)
 yield page
 context.close()
 browser.close()
 
 
@pytest.fixture(scope="function")
def set_up_excel(playwright: Playwright) -> None:
 browser= playwright.chromium.launch(headless=False, slow_mo=400)
 context= browser.new_context()
 context=browser.new_context(viewport={'width':1500, 'height':800})
 page=context.new_page()
 url="https://demoqa.com/automation-practice-form"
 page.goto(url)
 expect(page).to_have_title("DEMOQA")
 
 #context.tracing.start(screenshots=True, snapshots=True,sources=True)
 #context.tracing.stop(path="trace.zip")
 page.set_default_timeout(5000)
 yield page
 context.close()
 browser.close()
 