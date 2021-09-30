import time
import os
from selenium import webdriver
from random import randint

class LinkedinCrawler():
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')
        
        self.login_linkedin(
            os.environ['email'],
            os.environ['senha']
        )

        for page in range(1,3):
            self.procurar_recrutadores(page)

        self.driver.quit()

    def procurar_recrutadores(self, page):
        self.driver.get(
            f'https://www.linkedin.com/search/results/people/?geoUrn=%5B%22106057199%22%5D&keywords=tech%20recruiter&network=%5B%22S%22%5D&origin=FACETED_SEARCH&page={page}&position=0&searchId=89476201-25c0-4675-ba24-caac705b9256&sid=%2C(M'
        )
        self.tempo_espera_aleatorio(10, 20)

        for recrutador_button in self.driver.find_elements_by_css_selector('div.entity-result__item div.entity-result__actions.entity-result__divider div button'):
            recrutador_button.click()
            time.sleep(3)
            self.driver.find_element_by_css_selector('button.ml1.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view').click()
            self.tempo_espera_aleatorio(5, 10)

    def login_linkedin(self, email, senha):
        self.driver.get('https://www.linkedin.com/feed/')

        time.sleep(5)

        aviso_logoff = self.buscar_xpath_page('/html/body/div[1]/main/form/header/h1')
        if aviso_logoff != None:
            self.driver.get('https://www.linkedin.com/uas/login')

            self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(email)
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(senha)
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()

            time.sleep(5)
        else:
            time.sleep(2)

    def buscar_xpath_page(self, xpath):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except:
            return None

    def tempo_espera_aleatorio(self, initial, final):
        numero_aleatorio = randint(initial, final)
        print (f'ESPERANDO {numero_aleatorio} SEGUNDOS')
        time.sleep(numero_aleatorio)

LinkedinCrawler()