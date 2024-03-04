import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright


class Funciones_Globales:
    #Constructor
    def __init__(self,page):
        self.page=page
        
        
    def Esperar(self,tiempo=0.5):
         time.sleep(tiempo)
         
             
    def Scroll_xy(self,x,y,tiempo=0.5):
         self.page.mouse.wheel(x,y)
         time.sleep(tiempo)
         
         
    def Texto(self,selector,texto,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        expect(t).to_be_empty()
        t.highlight()
        t.fill(texto)
        t=self.page.get_by_label(texto)
        time.sleep(tiempo)
        
        
    def Click(self,selector,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.click()
        #t=self.page.get_by_label(texto)
        time.sleep(1)
        
        
    def combo_value(self,selector,valor,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.select_option(label=valor)
        time.sleep(1)
         
    def Upload_File(self,selector,archivo,tiempo):
        
     self.page.locator(selector).set_input_files(archivo)
     time.sleep(tiempo)
         
    def Upload_File_remove(self,selector,tiempo):
        
     self.page.locator(selector).set_input_files([])
     time.sleep(tiempo)
    
         
    def Click_first(self,selector,tiempo=0.5):
        self.page.locator(selector).first.click()
        time.sleep(tiempo)