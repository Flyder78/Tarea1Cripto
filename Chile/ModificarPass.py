from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Edge(executable_path=r"D:\Universidad\2021\Practica\Chrome_driver\msedgedriver.exe")
driver.get("https://www.niusushi.cl")
driver.execute_script('document.querySelector("#signin-signout").click()')

time.sleep(1)
mail=driver.find_element_by_xpath('//*[@id="login-email"]')
mail.send_keys("vcroninr_f885t@gexik.com")
time.sleep(1)
clave=driver.find_element_by_xpath('//*[@id="login-password"]')
time.sleep(1)
clave.send_keys('poder123')
time.sleep(1)
driver.execute_script('document.querySelector("#login-btn").click()')
time.sleep(1)
driver.execute_script('document.querySelector("#customer-name").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > div.modal.fade.ng-isolate-scope.in > div > div > div > div > div > a:nth-child(2)").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > div.wrapper-ov.ng-scope > div > div.header-perfil.row > div.col-md-4 > div > a:nth-child(1) > p").click()')
time.sleep(1)
newpass=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/fieldset/div/input')
newpass.send_keys("letsgo")
time.sleep(1)
driver.execute_script('document.querySelector("body > div.modal.fade.ng-isolate-scope.in > div > div > div > form > fieldset > button").click()')
time.sleep(5)
driver.close()

