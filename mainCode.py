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
def obtenerPartesURL(archivo):
    navegacion = separarColumnas('navegacion.csv')
    Df = pd.DataFrame(navegacion.loc[:, 'url_landing'])#, columns = ['camp', 'adg', 'device', 'adv', 'sl'])
    Df.to_csv('url_landing.csv')
    print(Df)

    new_df = pd.read_csv('url_landing.csv')
    new_df = pd.loc[:, 'url_landing']

    new_df = pd.DataFrame(new_df, columns = ['url_landing','idUser', 'uuid', 'camp', 'adg', 'device', 'sl', 'adv', 'rec'])

