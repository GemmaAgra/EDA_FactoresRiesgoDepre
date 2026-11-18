import numpy as np
import pandas as pd
import utils
from pathlib import Path


class Depresion:

    def __init__(self):

        BASE_DIR = Path(__file__).resolve().parent              # Obtener la carpeta donde está main.py   
        ruta_excel = BASE_DIR / 'Data' / 'BD_depresion.xlsx'    # Construir la ruta del Excel     
        self.df = pd.read_excel(ruta_excel, engine='openpyxl')   # Cargar el DataFrame como atributo del objeto        


if __name__ == "__main__":

    D = Depresion()
    print(D.df.head())

    utils.hipotesis_H1(D.df)   # envio el D.df a la función
    utils.hipotesis_H2(D.df)
    utils.hipotesis_H3(D.df)