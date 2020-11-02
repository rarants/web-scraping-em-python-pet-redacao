from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# URL
url = "https://www.ufsm.br/cursos/graduacao/santa-maria/sistemas-de-informacao/informacoes-do-curriculo"

# Configura as opções para que não seja aberta a guia durante a execução
option = Options()
option.headless = True

# Como parâmetro, passamos a nossa configuração (opcional: sem parâmetros, abre por padrão a guia)
driver = webdriver.Chrome(options=option)

# Buscamos os dados da URL
driver.get(url)

# Buscamos e acionamos o botão
btn_more = driver.find_element(By.ID, 'collapse-heading-curso_disciplinas_semestre__1250_1')
btn_more.click()

driver.quit()
