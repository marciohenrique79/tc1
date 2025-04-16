import requests
from bs4 import BeautifulSoup
import pandas as pd

ANO_FINAL = 2023

# Realiza a busca de um único ano específico
def raspagemUnit(ano=ANO_FINAL,opcao='opt_02'):
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao="+opcao+"&ano="+str(ano)
    response = requests.get(url)

    # Verifica se a requisição foi bem sucedida
    response.raise_for_status()

    # Parse do HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    tabela = soup.find('table', {'class':'tb_base tb_dados'})
    rows = tabela.find_all('tr')
    data = []

    for row in rows:
        cells = row.find_all(['th','td'])
        cells_text = [cell.get_text(strip=True) for cell in cells]
        data.append(cells_text)

    df = pd.DataFrame(data[1:],columns=data[0]) # linha 0 é o cabeçalho
    #df = pd.DataFrame(data[1:])
    df.head()