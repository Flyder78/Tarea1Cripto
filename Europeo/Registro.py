from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Edge(executable_path=r"D:\Universidad\2021\Practica\Chrome_driver\msedgedriver.exe")
driver.get("https://www.filmin.es")
driver.execute_script('document.querySelector("body > div.layout__header > header > div.site-header--on-desktop.align-items-center > a.ml-3.c-button.c-button--sm.c-button--light.c-button--outline").click()')
time.sleep(1)
boton=driver.find_element_by_xpath('/html/body/div[2]/div[1]/main/div[3]/div[1]/button').click()
#probar otro correo poque este ya se uso
time.sleep(1)
mail=driver.find_element_by_xpath('//*[@id="email"]')
mail.send_keys("beau00k_c159m@pebih.com")
time.sleep(1)
clave=driver.find_element_by_xpath('//*[@id="password"]')
time.sleep(1)
clave.send_keys('1234567')
time.sleep(1)
driver.execute_script('document.querySelector("#signUp > form > div.my-4 > button").click()')
time.sleep(5)
driver.close()
