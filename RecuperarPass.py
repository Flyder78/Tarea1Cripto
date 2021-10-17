from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Edge(executable_path=r"D:\Universidad\2021\Practica\Chrome_driver\msedgedriver.exe")
driver.get("https://www.filmin.es")
driver.execute_script('document.querySelector("body > div.layout__header > header > div.site-header--on-desktop.align-items-center > a.ml-3.c-button.c-button--sm.c-button--light.c-button--outline").click()')
driver.execute_script('document.querySelector("#signIn > form > div.form-group.mb-4 > button").click()')
#este tiempo debe varias segun cuanto se demore en cargar la alerta
time.sleep(5)
mail=driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/div[1]/input')
mail.send_keys("adam13w_n335e@pebih.com")
time.sleep(1)
driver.execute_script('document.querySelector("#reset-form-submit").click()')
time.sleep(5)
driver.close()