import re
from numpy.core.numeric import NaN
import pandas as pd
from pandas.core.frame import DataFrame
import urllib

def leerdatos(archivo):
    return pd.read_csv(archivo, sep = ';')

def mostrar_datos(archivo):
    print(archivo)

navegacion = leerdatos('navegacion.csv')
conversion = leerdatos('conversiones.csv')
print(len(navegacion))
Df = navegacion['url_landing'].str.split('&', expand = True)
print(len(Df))
Df.columns = ['url_landing','idUser', 'uuid', 'camp', 'adg', 'device', 'sl', 'adv', 'rec', 'vacía']
Df.drop(['vacía'], axis=1) #1 es columnas para las columnas
new_df = Df['url_landing'].str.split('/', 4, expand = True)
new_df = new_df.drop(new_df.columns[[0, 1, 2, 3]], axis = 'columns')
modelo = new_df[new_df.columns[0]].str.split('/', expand = True)
modelo = modelo.drop(modelo.columns[2], axis = 1)
print(str.__contains__(modelo.loc[0, modelo.columns[0]], 'gclid'))
print(len(modelo))

# for i in range(0, len(modelo)):
#     if str.__contains__(modelo.loc[i, modelo.columns[0]], 'gclid'):
#         modelo.loc[i, modelo.columns[1]] = modelo.loc[i, modelo.columns[0]]
#         modelo.loc[i, modelo.columns[0]] = NaN

# print(modelo.head())
