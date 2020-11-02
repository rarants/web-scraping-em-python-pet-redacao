# Importar bibliotecas
import requests 
from bs4 import BeautifulSoup 

# Função que busca o soup
def get_soup(url):
    # get retorna um objeto, com alguns atributos, como content e status_code
    html = requests.get(url)

    # Verificar se houve falha na requisição (status_code == 200, significa que foi bem-sucedida)
    if html.status_code != 200: 
        print(">> Falha na requisição! <<")
    else:
        # content passa o conteúdo da página
        html_content = html.content

    # Parsear o conteúdo HTML buscado, para poder ficar mais estruturado de acordo com as tags HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Retorna o soup
    return soup