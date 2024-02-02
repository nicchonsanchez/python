from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://nicchon.com")
time.sleep(2)
navegador.find_element('xpath', '/html/body/header/nav/ul/li[3]/a/div/p').click()
time.sleep(5)