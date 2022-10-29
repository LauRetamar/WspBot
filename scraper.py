from ast import keyword
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time

#enter: "\ue007",


def SendMessageTo(name, message, url, quantity):
    
    chromeOptions = Options()
    chromeOptions.add_experimental_option("debuggerAddress","localhost:9250")

    userDataDir = os.getcwd() + "/cookies"
    chromeOptions.add_argument("user-data-dir=" + userDataDir)

    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(url)

    driver.implicitly_wait(10)

    searchInput = driver.find_element(By.XPATH, "//div[@title='Cuadro de texto para ingresar la búsqueda']")
    
    searchInput.send_keys(name)

    driver.implicitly_wait(1)

    nameLabel = driver.find_element(By.XPATH, f"//span[@title='{name}']")
    nameLabel.click()

    for x in range(0, int(quantity)):

        messageInput = driver.find_element(By.XPATH, "//div[@title='Escribe un mensaje aquí']")
        messageInput.send_keys(message)
        messageInput.send_keys(Keys.RETURN)

    driver.quit()