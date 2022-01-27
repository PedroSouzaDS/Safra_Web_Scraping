import pandas as pd
from selenium import webdriver


class SafraScrapping():
    # inicia acesso a plataforma
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://epfweb.safra.com.br/Home/Login?forcarLoginManual=S')
        self.login = str(input(r'Login (evite erros copiando e colando): '))
        self.senha = str(input(r'Senha (evite erros copiando e colando): ')) 