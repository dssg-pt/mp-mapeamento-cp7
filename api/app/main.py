from typing import Optional

from fastapi import FastAPI, HTTPException

import sqlite3

app = FastAPI()

@app.on_event('startup')
def startup():
    global db_conn, cur

    db_path = 'db/cod_post_freg_matched.db'
    db_conn = sqlite3.connect(db_path, check_same_thread=False)
    cur = db_conn.cursor()

@app.on_event("shutdown")
def shutdown():
    db_conn.disconnect()

@app.get("/{cod_postal}")
def read_item(cod_postal: int):
    db_entry = cur.execute(f'''SELECT CodigoPostal, Distrito, Concelho, Freguesia FROM cod_post_freg
                              WHERE CodigoPostal = {cod_postal}''').fetchall()
    if not len(db_entry):
        raise HTTPException(status_code=404, detail='Codigo postal não encontrado na base de dados.')
    elif None in db_entry[0]:
        raise HTTPException(status_code=404, detail='Informação sobre código postal em falta.')

    keys = ['CodigoPostal', 'Distrito', 'Concelho', 'Freguesia']
    return {0: {key: val for key, val in zip(keys, db_entry[0])}}