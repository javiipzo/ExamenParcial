import re
from numpy.core.numeric import NaN
import pandas as pd
from pandas.core.frame import DataFrame
import urllib

def leerdatos(archivo):
    return pd.read_csv(archivo, sep = ';')

def mostrar_datos(archivo):
    print(archivo)
    #para separar toda la url
def separar_url(archivo):
    navegacion = leerdatos(archivo)
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
separar_url("navegacion.csv")
    #para ver unicamente los idUser
def usuariosRepes(archivo):
    df=pd.read_csv(archivo,header=0, sep=";")
    navegacion = leerdatos(archivo)

    Df = navegacion['url_landing'].str.split('&', expand = True)
    Df.columns = ['url_landing','idUser', 'uuid', 'camp', 'adg', 'device', 'sl', 'adv', 'rec',' ']
    Ddf=Df.drop(['url_landing','uuid','camp','adg','device','sl','adv','rec'], axis=1)
    print(Ddf.head())
    print("\n")

<<<<<<< HEAD
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
=======
>>>>>>> bbe230c55f83235ce547a77f28420aa0666757ee
