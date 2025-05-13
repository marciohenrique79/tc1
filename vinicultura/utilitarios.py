import pandas as pd
import json

def recupera_csv(rota=str,ano=str):
    match rota:
        case 'producao':
            df = pd.read_csv("csv\Producao.csv",delimiter=";")            
            return {"titulo": "Produção de vinhos e derivados",
                    "ano": str(ano),
                    "tipo": [df[['produto',str(ano)]].to_json()]
                }
        case 'processamento':
            df = pd.read_csv("csv\ProcessaViniferas.csv",delimiter=";")
            j1 = df[['cultivar',str(ano)]].to_json()
            df = pd.read_csv("csv\ProcessaAmericanas.csv",delimiter="\t")
            j2 = df[['cultivar',str(ano)]].to_json()
            df = pd.read_csv("csv\ProcessaMesa.csv",delimiter="\t")
            j3 = df[['cultivar',str(ano)]].to_json()
            df = pd.read_csv("csv\ProcessaSemclass.csv",delimiter="\t")
            j4 = df[['cultivar',str(ano)]].to_json()
            return {"titulo": "Processamento",
                    "ano": str(ano),
                    "tipo": {"Viníferas":j1, "Americanas":j2,"Mesa":j3,"Sem Classe":j4}
                }            
        case 'comercializacao':
            df = pd.read_csv("csv\Comercio.csv",delimiter=";")
            return {"titulo": "Comercialização de vinhos e derivados",
                    "ano": str(ano),
                    "tipo": [df[['Produto',str(ano)]].to_json()]
                }            
        case 'importacao':
            df = pd.read_csv("csv\ImpVinhos.csv",delimiter="\t")
            j1 = df[['País',str(ano)]].to_json()
            df = pd.read_csv("csv\ImpEspumantes.csv",delimiter="\t")
            j2 = df[['País',str(ano)]].to_json()
            df = pd.read_csv("csv\ImpFrescas.csv",delimiter="\t")
            j3 = df[['País',str(ano)]].to_json()
            df = pd.read_csv("csv\ImpPassas.csv",delimiter="\t")
            j4 = df[['País',str(ano)]].to_json()
            df = pd.read_csv("csv\ImpSuco.csv",delimiter=";")
            j5 = df[['País',str(ano)]].to_json()
            return {"titulo": "Importação",
                    "ano": str(ano),
                    "tipo": {"Vinhos":j1, "Espumantes":j2,"Frescas":j3,"Passas":j4,"Suco":j5}
                }
        case 'exportacao':
            df = pd.read_csv("csv\ExpVinho.csv",delimiter="\t")
            j1 = df[['País',str(ano)]].to_json()
            df = pd.read_csv("csv\ExpEspumantes.csv",delimiter="\t")
            j2 = df[['País',str(ano)]].to_json()
            df = pd.read_csv("csv\ExpUva.csv",delimiter="\t")
            j3 = df[['País',str(ano)]].to_json()
            df = pd.read_csv("csv\ExpSuco.csv",delimiter="\t")
            j4 = df[['País',str(ano)]].to_json()            
            return {"titulo": "Exportação",
                    "ano": str(ano),
                    "tipo": {"Vinhos":j1, "Espumantes":j2,"Frescas":j3,"Suco":j4}
                }