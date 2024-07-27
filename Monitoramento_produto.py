from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup 
from time import sleep
import pandas as pd
import datetime
import schedule
import logging
import re
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%m-%Y %H:%M:%S')
os.system('cls')

#função de extraçao de dados
def dados_prod():
    dic = {'data':[],'nome':[],'valor':[],'link':[]}
    url_page = 'https://www.casasbahia.com.br/apple-iphone-15-pro-max-256-gb-titanio-azul/p/55064634?utm_campaign=DescontoEspecial&utm_medium=BuscaOrganica&utm_source=Google'
    browser_options = Options()
    browser_options.add_argument('--headless')

    with webdriver.Firefox(options=browser_options) as driver:
        try:
            driver.get(url_page)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            item = soup.find('div', class_='css-0 e1c9wg812')
            
            if item:
                nome = item.find('div', class_='dsvia-box css-tv497f').get_text().strip()
                nome = re.sub(r'\(.*$', '', nome).strip()
                dic['nome'].append(nome)
                
                valor = item.find('p', id='product-price').find_next('span').get_text()
                valor = valor.replace('.', '').replace(',', '.').replace('por R$','')
                valor_float = float(valor)
                dic['valor'].append(int(valor_float) if valor_float.is_integer() else valor_float)
                
                dic['link'].append(url_page)
                dic['data'].append(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        except Exception as e:
            logging.info(f'Erro ao carregar a página com Selenium: {e}')
    
    return dic

# Função para atualizar o arquivo CSV com os novos dados
def atualizar_csv(dic_produtos):
    df = pd.DataFrame(dic_produtos)
    arquivo_csv = 'DestravaDev/monitoramento_produto.csv'
    if os.path.exists(arquivo_csv):
        df_existing = pd.read_csv(arquivo_csv, sep=';')
        df_combined = pd.concat([df_existing, df], ignore_index=True)
        df_combined.to_csv(arquivo_csv, encoding='utf-8', sep=';', index=False)
        logging.info('Planilha atualizada com sucesso!')
    else:
        df.to_csv(arquivo_csv, encoding='utf-8', sep=';', index=False)
        logging.info('Planilha criada e atualizada com sucesso!')

# Função principal que coleta dados e atualiza o CSV
def tarefa_programada():
    dic_produtos = dados_prod()
    atualizar_csv(dic_produtos)

# Agenda a execução da função a cada 30 minutos
def agendar_prog():
    schedule.every(30).minutes.do(tarefa_programada)

# Loop principal que executa as tarefas agendadas
if __name__ == "__main__":
    logging.info("Programa em andamento...")

    agendar_prog()
    
    while True:
        schedule.run_pending()
        sleep(1)
