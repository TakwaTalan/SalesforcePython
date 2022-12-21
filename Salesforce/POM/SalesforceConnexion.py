from selenium import webdriver
from selenium.webdriver.common.by import By

class basePage():
    driver = webdriver.Chrome(executable_path="C:/Users/ttouzni/PycharmProjects/Salesforce/drivers/chromedriver.exe")
    driver.get("https://login.salesforce.com/?locale=fr")
    driver.maximize_window()
    login = driver.find_element(By.XPATH,"//input[@id='username']")
    login.send_keys("takwa.touzni@empathetic-koala-9d5ozw.com")
    Motdpasse = driver.find_element(By.XPATH, "//input[@id='password']")
    Motdpasse.send_keys("Talan2022**")
    Connecter = driver.find_element(By.XPATH, "//input[contains(@id,'Login')]")
    Connecter.click()
    driver.implicitly_wait(10)
    Configuration = driver.find_element(By.XPATH, "//*[@class='slds-icon-waffle']")
    Configuration.click()
    Ventes = driver.find_element(By.XPATH, "//lightning-input/div/input")
    Ventes.send_keys("Ventes")
    Ventes_btn = driver.find_element(By.XPATH, "(//*[@class='slds-truncate']/b)")
    Ventes_btn.click()

