import re
import time
import random
import pytest
import sys
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from Funciones import Funciones_Globales
from configtest import set_up, set_up_parametrizar


# primero correr de formar normal y despues ejecutar el comando(playwright show-trace trace.zip)
# playwright show-trace trace.zip
#pytest Multiples_test.py -s -v
#pytest Parametrizar.py -s -v
#grabar playwright codegen https://demoqa.com/automation-practice-form

pdf1="C:/Users/rodri/Videos/Playwrite/Curso/Estudiantes/Ejemplos/PDF/dgmn-certificado-de-situacion-militar-17276128.pdf"
@pytest.mark.parametrize("nombre,apellido",[("Rodrigo","Vizama"),("Alejandro","Vizama"),("Ron","Vizama")])
def test_Inicio(set_up_parametrizar,nombre,apellido) -> None:
 page=set_up_parametrizar
 #Creando nuestro objeto de tipo funciones globales
 F=Funciones_Globales(page)
 #time.sleep(2)
 #page.mouse.wheel(0,400)
 F.Scroll_xy(0,400)
 F.Texto("//input[contains(@placeholder,'First Name')]",nombre,2)
 F.Texto("//input[contains(@placeholder,'Last Name')]",apellido,2)
 F.Esperar(1)
 
 