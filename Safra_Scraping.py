import pandas as pd
import time
import random as rd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SafraScrapping():
    
    # INICIALIZALÇÃO
    def __init__(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://epfweb.safra.com.br/Home/Login?forcarLoginManual=S')
        login_safra = str(input(r'Login (evite erros copiando e colando): ')) 
        senha_safra = str(input(r'Senha (evite erros copiando e colando): ')) 
        self.login = login_safra
        self.senha = senha_safra
        time.sleep(rd.uniform(2,3))
        self.driver.find_element_by_id('txtUsuario').send_keys(self.login)
        time.sleep(rd.uniform(2.1,3.2))
        self.driver.find_element_by_id('txtSenha').send_keys(self.senha)
        time.sleep(rd.uniform(3,3.5))
        self.driver.find_element_by_id('btnEntrar').click()
        time.sleep(rd.uniform(2.8,3.8))
        
    # CONFIGURA ACESSO À DADOS DESEJADOS (PERCORRE CAMINHO ATÉ AS TABELAS ATIVAS)
    def acess_config(self):
        self.driver.find_element_by_xpath('//*[@id="browser"]/li/span').click()
        time.sleep(rd.uniform(1,2.2))
        self.driver.find_element_by_xpath('//*[@id="ulMenu"]/li[10]/span').click()
        time.sleep(rd.uniform(1,2.2))
        self.driver.find_element_by_xpath('//*[@id="ulMenu"]/li[10]/ul/li/span/a').click()
        time.sleep(rd.uniform(1,2.2))
        
    # PREENCHE FILTROS COM CONFIGURAÇÕES DAS TABELAS DESEJADAS (ATIVAS)
    def fill_forms(self):   
        '''FUNCAO AINDA INCOMPLETA, MOTIVO: A PAGINA DO SAFRA JA INICIALIZA ESTA PARTE COM TODOS OS 
        PARAMETROS DESEJADOS PREENCHIDOS. POREM, FUTURAMENTE PREENCHER POR MEDIDA DE SEGURANCA, ISTO E, 
        CASO A PLATAFORMA ALTERE O PADRAO DE PREENCHIMENTO PARA OUTRO NAO DESEJADO.
        '''
        self.driver.find_element_by_xpath('//*[@id="btnPesquisarCadastro"]/span').click()
# =============================================================================
#         time.sleep(rd.uniform(1.8,2.8))
#         self.driver.find_element_by_xpath('//*[@id="ddlFiltroCorbanSub_chzn"]/a/div/b').send_keys('3758 CORPORAÇÕES CEDIBRA LTDA' + Keys.ENTER)
#         self.driver.find_element_by_xpath('//*[@id="ddlFiltroCorban_chzn"]/a/div/b').send_keys('13083 CEDIBRA' + Keys.ENTER)
#         time.sleep(rd.uniform(1.8,2.8))
#         self.driver.find_element_by_xpath('//*[@id="ddlFiltroSituacao_chzn"]/a/div/b').send_keys('ATIVA' + Keys.ENTER)
#         time.sleep(rd.uniform(1.8,2.8))
#         self.driver.find_element_by_xpath('//*[@id="ui-accordion-divPrincipal-header-1"]/span').click()
#         time.sleep(rd.uniform(1.8,2.8))
# =============================================================================
    
    # ACESSA ABA DAS TABELAS ATIVAS
    '''
    ESTA ETAPA ACAOMPANHARA A SEQUENCIA DE MELHORIAS DA FUNCAO ANTERIOR.
    '''
    
    # BAIXA "TABELAS RESUMO - PDF" ITERADAMENTE (DIRECIONANDO PARA PASTA DOCUMENTOS NO COMPUTADOR)
    
    # CRIA TABELA "Safra_Sacraping" NO MODELO "CGR" EM PANDAS
    
    # COLETA DADOS DE "TABELAS RESUMO - PDF" E SALVA NA TABELA "Safra_Scraping - PANDAS" NAS RESPECTIVAS COLUNAS
    
    # CONVERTE VALORES DAS COLUNAS NOS TIPOS A SEREM USADOS NOS CÁLCULOS DAS TABELAS EM EXCEL
    
    # CRIA E EXPORTA PLANILHA "Safra_Scraping.xlsx" COMPLETA NA PASTA DOCUMENTOS
        
    
safra = SafraScrapping()        
safra.acess_config()
safra.fill_forms()
        

        