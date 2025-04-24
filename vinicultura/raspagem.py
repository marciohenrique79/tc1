import requests
from bs4 import BeautifulSoup
import pandas as pd
from json import loads, dumps

ANO_FINAL = 2023

def teste_var():
  return ANO_FINAL

#Extrai informação de todos os anos disponíveis para uma determinada opção
def raspagemTotal(opcao:str='opt_02'):
  df = pd.DataFrame()
  for ano in range(1970, ANO_FINAL+1):
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao={opcao}&ano={ano}"
    response = requests.get(url)

    #Verifica se a requisição foi bem sucedida
    response.raise_for_status()

    #Parse do HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    tabela = soup.find('table', {'class':'tb_base tb_dados'})
    rows = tabela.find_all('tr')
    data = []

    for row in rows:
      cells = row.find_all(['td'])
      cells_text = [cell.get_text(strip=True) for cell in cells]
      data.append(cells_text)

    if df.size == 0:
        df = pd.DataFrame(data[1:],columns=['Produto',str(ano)]) #
    else:
      qtd = []
      for item in data[1:]:
        qtd.append(item[1])
      df[str(ano)] = qtd

  df.to_csv('vitibrasil.csv', index=False)
  return df.to_json(orient="split")


# Realiza a busca de um único ano específico
def raspagemUnit(opcao='opt_02',ano=ANO_FINAL):
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
    #df.head()
    #result = df.to_json(orient="split")
    return df.to_json(orient="split")    