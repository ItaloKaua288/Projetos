import requests
from bs4 import BeautifulSoup
import pandas as pd

while True:
    nome = input('Digite o tipo do produto: ').strip()
    if nome != '':
        break
  
url = f'https://lista.mercadolivre.com.br/{nome}#D[A:{nome}]'

site = requests.get(url)
soup = BeautifulSoup(site.text, 'html.parser')

produtos = soup.find_all('div', class_='ui-search-result__content-wrapper shops__result-content-wrapper')
lista = []

for produto in produtos:
    dados = {}
    simbolo = produto.find('span', attrs={'class': 'price-tag-symbol'}).get_text()
    valor = produto.find('span', attrs={'class': 'price-tag-fraction'}).get_text()
    nome = produto.h2.text
    preco = simbolo + ' ' + valor
    avaliacao = produto.find('span', attrs={'class': 'ui-search-reviews__amount'})
    link = produto.find('a', attrs={'class': 'ui-search-link'}).get_attribute_list('href')

    dados['nome'] = nome
    dados['preço'] = preco
    if avaliacao != None:
        dados['avaliações'] = avaliacao.text
    else:
        dados['avaliações'] = None
    dados['link'] = link[0]
    lista.append(dados)

lista_df = pd.DataFrame(lista)
print(lista_df)
while True:
    salvar = input('Deseja salvar dados (Y/N)? ').strip().upper()
    if salvar == 'Y' or salvar == 'SIM':
        pd.DataFrame.to_excel(lista_df, excel_writer='data.xlsx', index=False)
        quit()
    elif salvar == 'N' or salvar == 'NOT' or salvar == 'NO':
        quit()
    else:
        print('Try again!')
        continue
