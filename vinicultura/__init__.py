# Importa os módulos necessários dentro da biblioteca Vinicultura
from .raspagem import raspagemTotal, raspagemUnit, ANO_FINAL

# Definição de valores globais para uso da aplicação
PROCESSAMENTO_VALIDOS = ('viniferas', 'americanas', 'uvas_de_mesa', 'sem_classificacao')
IMPORTACAO_VALIDOS = ('vinhos_de_mesa', 'espumantes', 'uvas_frescas', 'uvas_passas', 'suco_de_uva')
EXPORTACAO_VALIDOS = ('vinhos_de_mesa', 'espumantes', 'uvas_frescas', 'suco_de_uva')

LISTA_OPCOES = {
    2: 'producao',
    3: 'processmento',
    4: 'comercializacao',
    5: 'importacao',
    6: 'exportacao'
}

"""
# Verifica se as dependências estão instaladas
try:    
    import requests
except:
    print("Erro de dependência: biblioteca 'requests' não está instalada.")

try:    
    import bs4
except:
    print("Erro de dependência: biblioteca 'BeautifulSoup' não está instalada.")

try:    
    import pandas
except:
    print("Erro de dependência: biblioteca 'pandas' não está instalada.")

try:    
    import json
except:
    print("Erro de dependência: biblioteca 'json' não está instalada.")
"""