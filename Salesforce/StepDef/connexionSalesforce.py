from POM import SalesforceConnexion as SC
from selenium import webdriver

class SalesforceConnexion():
    def test_login(self):
        self.basePage.driver
        self.basePage.login
        self.basePage.Motdpasse
        self.basePage.Connecter

    def test_navigate_to_sales_page(self):
        self.basePage.driver.implicitly_wait(20)
        self.basePage.Configuration
        self.basePage.Ventes