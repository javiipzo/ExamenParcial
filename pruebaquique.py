import re
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
import urllib

def leerdatos(archivo):
    return pd.read_csv(archivo, sep = ';')

# Cargamos los datos en una variable
navegacion = leerdatos('navegacion.csv')
conversion = leerdatos('conversiones.csv')
print(navegacion.tail())

# Obtenemos el resto de columnas a partir de la URL
Datos_de_URL = navegacion['url_landing'].str.split('&', expand = True)
Datos_de_URL.columns = ['url_landing','idUser', 'uuid', 'camp', 'adg', 'device', 'sl', 'adv', 'rec', 'vacía']

# Nos faltaría sacar el modelo de coche de la URL
modelo = Datos_de_URL['url_landing'].str.split('/', 4, expand = True)
modelo = modelo.drop(modelo.columns[[0, 1, 2, 3]], axis = 'columns')
modelo = modelo[modelo.columns[0]].str.split('/', expand = True)
modelo = modelo.drop(modelo.columns[2], axis = 1) # axis = 1 para referirse a las columnas

# Como hay URLs que no tienen modelo tenemos que cuadrar el dataframe
modelo = modelo.astype(str)

for i in range(0, len(modelo)):
    if str.__contains__(modelo.loc[i, modelo.columns[0]], 'gclid'):
        modelo.loc[i, modelo.columns[1]] = modelo.loc[i, modelo.columns[0]]
        modelo.loc[i, modelo.columns[0]] = NaN
    elif str.__contains__(modelo.loc[i, modelo.columns[0]], 'nan'):
        modelo.loc[i, modelo.columns[0]] = NaN
        modelo.loc[i, modelo.columns[1]] = NaN

modelo.columns = ['Modelo', 'gclid']
print(modelo.head())
print(modelo.tail())
print(len(modelo))

# Eliminamos la columna URL_landing modificados
Datos_de_URL = Datos_de_URL.drop(['url_landing', 'vacía'], axis = 1)
frames = [navegacion, Datos_de_URL, modelo]
Navegacion_final = pd.concat(frames)
print(Navegacion_final.head())
