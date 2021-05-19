from typing import Optional

from fastapi import FastAPI, HTTPException

import pandas as pd

app = FastAPI()

@app.on_event('startup')
def startup():
    global df

    url = 'https://raw.githubusercontent.com/dssg-pt/mp-mapeamento-cp7/main/output_data/cod_post_freg_matched.csv'
    df = pd.read_csv(url, index_col='CodigoPostal')

@app.get("/{cod_postal}")
def read_item(cod_postal: int):
    keys = ['Distrito', 'Concelho', 'Freguesia']

    try:
        df_entry = df.loc[cod_postal, keys]
    except KeyError:
        raise HTTPException(status_code=404, detail='Codigo postal não encontrado na base de dados.')

    if df_entry.isna().any():
        raise HTTPException(status_code=404, detail='Informação sobre código postal em falta.')
    
    df_entry_dict = df_entry.to_dict()
    df_entry_dict['CodigoPostal'] = cod_postal

    return {0: df_entry_dict}