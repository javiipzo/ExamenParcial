import pandas as pd
from pandas.core.frame import DataFrame
import urllib.parse
#import urllib3
#para leer el fichero
def leerdatos(archivo ):
    df = pd.read_csv(archivo)
    return df

#Separar todo en columnas
def separarColumnas(archivo):
    return pd.read_csv(archivo, sep=";")

#obtener todas las partes de la url, issue2
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
#para obtener unicamente el iduser, ya que el gclid y modelo ya se ha obtenido anteriormente:
def usuariosRepes(archivo):
    df=pd.read_csv(archivo,header=0, sep=";")
    navegacion = leerdatos(archivo)

    Df = navegacion['url_landing'].str.split('&', expand = True)
    Df.columns = ['url_landing','idUser', 'uuid', 'camp', 'adg', 'device', 'sl', 'adv', 'rec',' ']
    Ddf=Df.drop(['url_landing','uuid','camp','adg','device','sl','adv','rec'], axis=1)
    print(Ddf.head())
    print("\n")

usuariosRepes("navegacion.csv")