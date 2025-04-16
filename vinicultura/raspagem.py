import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame()
ANO_FINAL = 2023

#Extrai informação de todos os anos disponíveis
def raspagem(opcao='opt_02')
  for ano in range(1970, ANO_FINAL+1):
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02&ano="+str(ano)
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