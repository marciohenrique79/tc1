from fastapi import FastAPI, HTTPException

PROCESSAMENTO_VALIDOS = ('viniferas', 'americanas', 'uvas_de_mesa', 'sem_classificacao')
IMPORTACAO_VALIDOS = ('vinhos_de_mesa', 'espumantes', 'uvas_frescas', 'uvas_passas', 'suco_de_uva')
EXPORTACAO_VALIDOS = ('vinhos_de_mesa', 'espumantes', 'uvas_frescas', 'suco_de_uva')

#Controle de vesão
app = FastAPI(
    title="API - Embrapa",
    version="1.0.0",
    description="API - Embrapa - dados de Vinicultura"
)

# Autenticacao

#

@app.get("/")
async def boas_vindas():
    return {"message":"Embrapa - dados de Vinicultura"}

@app.get("/producao")
async def producao(ano=0):
    if ano:
        if ano in range(1970,2024):
            return {"message":f"Dados de produção do ano {ano}"}
        else:
             raise HTTPException(status_code=404, detail="Não há dados para o ano solicitado!")        
    else:
        return {"message":"Dados de produção de 1970 a 2023"}

@app.get("/processamento/{tipo}")
async def processamento(tipo:str="viniferas",ano:int=0):
    if tipo.lower() not in PROCESSAMENTO_VALIDOS:
        raise HTTPException(status_code=404, detail="Tipo de processamento não encontrado!")
    if ano:
        if ano in range(1970,2024):
            return {"message":f"Dados de processamento de {tipo} ano {ano}"}
        else:
             raise HTTPException(status_code=404, detail="Não há dados para o ano solicitado!")
    else:
        return {"message":f"Dados de processamento de {tipo} de 1970 a 2023"}

@app.get("/comercializacao")
async def comercializacao(ano=0):
    if ano:
        if ano in range(1970,2024):
            return {"message":f"Dados de comercialização do ano {ano}"}
        else:
             raise HTTPException(status_code=404, detail="Não há dados para o ano solicitado!")    
    else:
        return {"message":"Dados de comercialização de 1970 a 2023"}
    
@app.get("/importacao/{tipo}")
async def importacao(tipo:str="viniferas",ano:int=0):
    if tipo.lower() not in IMPORTACAO_VALIDOS:
        raise HTTPException(status_code=404, detail="Produto de importação não encontrado!")
    if ano:
        if ano in range(1970,2024):
            return {"message":f"Dados de importação de {tipo} ano {ano}"}
        else:
             raise HTTPException(status_code=404, detail="Não há dados para o ano solicitado!")        
    else:
        return {"message":f"Dados de importação de {tipo} de 1970 a 2023"}
    
@app.get("/exportacao/{tipo}")
async def exportacao(tipo:str="viniferas",ano:int=0):
    if tipo.lower() not in EXPORTACAO_VALIDOS:
        raise HTTPException(status_code=404, detail="Produto de exportação não encontrado!")
    if ano:
        if ano in range(1970,2024):
            return {"message":f"Dados de exportação de {tipo} ano {ano}"}
        else:
             raise HTTPException(status_code=404, detail="Não há dados para o ano solicitado!")        
    else:
        return {"message":f"Dados de exportação de {tipo} de 1970 a 2023"}
    
#if __name__ == "__main__":
#    main()