import pandas as pd
from pandas.core.frame import DataFrame
import urllib.parse
#import urllib3
#para leer el fichero
def leerdatos(archivo ):
    df = pd.read_csv(archivo)
    return df
#buscar un dato en concreto de un fichero a partir de la fila y columna
def getvalue(archivo,fila,dato):
    df = pd.read_csv(archivo)
    df._get_value(fila,dato)

#Separar todo en columnas
def separarColumnas(archivo):
    df=pd.read_csv(archivo, sep=";")

#obtener todas las partes de la url, issue2
def obtenerPartesURL(archivo,columna):
    df=pd.read_csv(archivo, sep=";")
    #primero obtengo la URL
    df.iloc[columna]
    partes = []
    partes.append (df.urllib.parse)
    print(partes)

obtenerPartesURL("navegacion.csv",5)

navegacion = separarColumnas('navegacion.csv')
conversion = separarColumnas('conversiones.csv')
Df = pd.DataFrame(navegacion.loc[:, 'url_landing'])#, columns = ['camp', 'adg', 'device', 'adv', 'sl'])
Df.to_csv('url_landing.csv') 
print(Df)

new_df = pd.read_csv('url_landing.csv')
new_df = pd.loc[:, 'url_landing']

new_df = pd.DataFrame(new_df, columns = ['url_landing','idUser', 'uuid', 'camp', 'adg', 'device', 'sl', 'adv', 'rec'])
