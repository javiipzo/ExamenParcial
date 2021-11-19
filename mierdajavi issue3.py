import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import urllib
def leerdatos(archivo):
    return pd.read_csv(archivo, sep = ';')

def mostrar_datos(archivo):
    print(archivo)

def usuariosRepes(archivo):
    df=pd.read_csv(archivo,header=0, sep=";")
    navegacion = leerdatos(archivo)

    print(navegacion.head())
    Df = navegacion['url_landing'].str.split('&', expand = True)
    print(Df.head())
    Df.columns = ['url_landing','idUser', 'uuid', 'camp', 'adg', 'device', 'sl', 'adv', 'rec',' ']
    Ddf=Df.drop(['url_landing','uuid','camp','adg','device','sl','adv','rec'], axis=1)
    print(Ddf.head())

usuariosRepes("navegacion.csv")