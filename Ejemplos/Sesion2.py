import re
import time
import random
import pytest
import sys
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from Funciones import Funciones_Globales
from configtest import set_up

# primero correr de formar normal y despues ejecutar el comando(playwright show-trace trace.zip)
# playwright show-trace trace.zip
#pytest Multiples_test.py -s -v
#grabar playwright codegen https://www.saucedemo.com/

pdf1="C:/Users/rodri/Videos/Playwrite/Curso/Estudiantes/Ejemplos/PDF/dgmn-certificado-de-situacion-militar-17276128.pdf"

def test_sesion1(set_up)-> None:
 page=set_up
 F=Funciones_Globales(page)
 
 def test_sesion2(set_up)-> None:
  page=set_up
 F=Funciones_Globales(page)

 F.Click("//button[contains(@id,'add-to-cart-sauce-labs-backpack')]",1)
 F.Click("//button[contains(@id,'add-to-cart-sauce-labs-bike-light')]",1)
 F.Esperar(tiempo=2)
    
 def test_sesion3(set_up)-> None:
  page=set_up
 F=Funciones_Globales(page)

 F.Click("//button[contains(@id,'react-burger-menu-btn')]",1)
 F.Click("//a[contains(@id,'link')][@class='bm-item menu-item'][contains(.,'Reset App State')]",1)
 F.Click("//button[contains(@id,'react-burger-cross-btn')]",1)
 F.Esperar(tiempo=2)
    
    