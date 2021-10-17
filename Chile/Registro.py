from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Edge(executable_path=r"D:\Universidad\2021\Practica\Chrome_driver\msedgedriver.exe")
driver.get("https://www.niusushi.cl")
driver.execute_script('document.querySelector("#signin-signout").click()')
#Cambiar variables porque estas ya se usaron
time.sleep(1)
mail=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/input[1]')
mail.send_keys("Pedritooooooooou")
time.sleep(1)
mail=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/input[2]')
mail.send_keys("adam13w_n335e@pebih.com")
time.sleep(1)
mail=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/div/div[2]/input')
mail.send_keys("65738553")
time.sleep(1)
clave=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/input[3]')
time.sleep(1)
clave.send_keys('poder123')
time.sleep(1)
driver.execute_script('document.querySelector("body > div.modal.fade.ng-isolate-scope.in > div > div > div:nth-child(2) > form > button").click()')
time.sleep(5)
driver.close()

