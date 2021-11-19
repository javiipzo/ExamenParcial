import re
import pandas as pd
from pandas.core.frame import DataFrame
import urllib

def leerdatos(archivo):
    return pd.read_csv(archivo, sep = ';')

def mostrar_datos(archivo):
    print(archivo)

navegacion = leerdatos('navegacion.csv')
conversion = leerdatos('conversiones.csv')
print(navegacion.head())
Df = navegacion['url_landing'].str.split('&', expand = True)
Df.columns = ['url_landing','idUser', 'uuid', 'camp', 'adg', 'device', 'sl', 'adv', 'rec', 'vacía']
Df.drop(['vacía'], axis=1) #1 es columnas para las columnas
print(Df.head())
new_df = Df['url_landing'].str.split('/', 4, expand = True)
new_df = new_df.drop(new_df.columns[[0, 1, 2, 3]], axis = 'columns')
print(new_df.head())
modelo = new_df[new_df.columns[0]].str.split('/', expand = True)
print(modelo.head())
