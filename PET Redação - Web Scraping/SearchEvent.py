# Importar bibliotecas
import requests as rq 
from bs4 import BeautifulSoup 

# Função que busca o conteúdo especificado
#   → Tag = tag HTML que estamos buscando
#   → Identifier = identificador da tag (id,spam, div, etc.)
#   → Desc = descrição da classe, spam, etc. (ex: class = "titulo-publicacao-widget", logo a desc é titulo-publicacao-widget)
def search(soup, tag, identifier, desc):
    event_found = soup.findAll(tag, {identifier: desc})
    return event_found