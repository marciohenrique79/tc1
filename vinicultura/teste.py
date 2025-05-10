import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from vinicultura.utilitarios import recupera_csv

#dados = recupera_csv('producao',1972)
#dados = recupera_csv('comercializacao',1997)
#dados = recupera_csv('processamento',2005)
#dados = recupera_csv('importacao',2018)
dados = recupera_csv('exportacao',2021)
print(dados)