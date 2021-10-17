from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Edge(executable_path=r"D:\Universidad\2021\Practica\Chrome_driver\msedgedriver.exe")
driver.get("https://www.niusushi.cl")
driver.execute_script('document.querySelector("#signin-signout").click()')
time.sleep(1)
driver.execute_script('document.querySelector("body > div.modal.fade.ng-isolate-scope.in > div > div > div:nth-child(1) > form > a").click()')
time.sleep(1)
mail=driver.find_element_by_xpath('/html/body/div[1]/div/div/form/fieldset/input')
mail.send_keys("adam13w_n335e@pebih.com")
time.sleep(1)
driver.execute_script('document.querySelector("body > div.modal.fade.ng-isolate-scope.in > div > div > form > fieldset > button").click()')
time.sleep(5)
driver.close()

