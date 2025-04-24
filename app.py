from fastapi import FastAPI, HTTPException
from vinicultura import raspagemTotal, raspagemUnit
from vinicultura import PROCESSAMENTO_VALIDOS, IMPORTACAO_VALIDOS, EXPORTACAO_VALIDOS

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
async def producao(ano:int=0):
    if ano:
        if ano in range(1970,2024):
            dados = raspagemUnit("opt_02",ano)
            return {"message":f"Dados de produção do ano {ano}:{dados}"}
        else:
             raise HTTPException(status_code=404, detail="Não há dados para o ano solicitado!")        
    else:
        dados = raspagemTotal("opt_02")
        return {"message":f"Dados de produção de 1970 a 2023: {dados}"}

@app.get("/processamento/{tipo}")
async def processamento(tipo:str="viniferas",ano:int=0):
    if tipo.lower() not in PROCESSAMENTO_VALIDOS:
        raise HTTPException(status_code=404, detail="Tipo de processamento não encontrado!")
    if ano:
        if ano in range(1970,2024):
            sub_opt = PROCESSAMENTO_VALIDOS.index(tipo.lower())+1
            dados = raspagemUnit(f"opt_03&subopt_0{sub_opt}",ano)
            return {"message":f"Dados de processamento de {tipo} ano {ano}:{dados}"}
        else:
             raise HTTPException(status_code=404, detail="Não há dados para o ano solicitado!")
    else:
        return {"message":f"Dados de processamento de {tipo} de 1970 a 2023"}

@app.get("/comercializacao")
async def comercializacao(ano:int=0):
    if ano:
        if ano in range(1970,2024):
            dados = raspagemUnit("opt_04",ano)
            return {"message":f"Dados de comercialização do ano {ano}:{dados}"}
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
            sub_opt = IMPORTACAO_VALIDOS.index(tipo.lower())+1
            dados = raspagemUnit(f"opt_05&subopt_0{sub_opt}",ano)
            return {"message":f"Dados de importação de {tipo} ano {ano}:{dados}"}
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
            sub_opt = EXPORTACAO_VALIDOS.index(tipo.lower())+1
            dados = raspagemUnit(f"opt_06&subopt_0{sub_opt}",ano)
            return {"message":f"Dados de exportação de {tipo} ano {ano}:{dados}"}
        else:
             raise HTTPException(status_code=404, detail="Não há dados para o ano solicitado!")        
    else:
        # 
        return {"message":f"Dados de exportação de {tipo} de 1970 a 2023"}
    
#if __name__ == "__main__":
#    main()