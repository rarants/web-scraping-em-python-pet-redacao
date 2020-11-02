# Importar bibliotecas
import pandas 
from GetSoup import get_soup
from SearchEvent import search

# Função auxiliar para formatar os títulos
def format_text(element):
    text = element.text.title()
    return text

# Criamos um dicionário vazio para adicionar os eventos futuramente e listas para armazenar os títulos e datas dos eventos
events = {}
titles = []
dates = []

# Buscamos o conteúdo HTML a partir da URL do site, então adicionamos a URL a uma var
url = "https://www.ufsm.br/"

# Buscar o soup
soup = get_soup(url)

# Extraímos o dado desejado. Neste caso, selecionamos os títulos dos eventos
found_titles = search(soup, "span", "class", "titulo-publicacao-widget")
found_dates  = search(soup, "div",  "class", "data-publicacao-widget")

# Salvamos os dados buscados em um dicionário
for i in range(0, len(found_titles)-1):
    titles.insert(i,format_text(found_titles[i]))
    dates.insert(i, format_text(found_dates[i]))

events.update({"Name": titles, "Date" : dates})

# Usando a biblioteca Pandas, podemos estruturar os dados
data_frame = pandas.DataFrame(data=events)

# Exibe no console os eventos organizados pela pandas
print("\nEVENTOS {}:\n{}".format(url, data_frame))