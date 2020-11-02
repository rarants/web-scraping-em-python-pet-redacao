import pandas 
import json
from GetSoup import get_soup
from SearchEvent import search
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Vamos converter a tabela em um dicionário, então iremos iniciá-lo aqui
horarios = {}

# Salvar URL em uma var
url = "https://www.ufsm.br/onibus-horarios?linha=UFSM%20BOMBEIROS&dia=DIAS%20ÚTEIS"

# Buscar o soup
soup = get_soup(url)

# Extraímos o dado desejado. 
found_table = search(soup, "div", "class", "col-lg-6 informativo_horarios")

# Usando a biblioteca Pandas, podemos estruturar os dados
data_frame = pandas.read_html(str(found_table))[0]

# Se quisermos limpar os dados, podemos fazer o seguinte: 
# df = data_frame[['Hora', 'Detalhe']]  # Listar as colunas da tabela
# df.columns = ['Hora', 'Detalhe']      # Listar as colunas que iremos manter

# Convertemos o data frame para um dicionário
horarios['Horarios'] = data_frame.to_dict('records')

# Podemos salvar como um json o nosso dicionário:
# Abrimos um novo arquivo em modo de escrita (w)
new_json = json.dumps(horarios)
new_file = open("horarios.json", "w")
new_file.write(new_json)
new_file.close()

