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
    partes = urllib.parse
    return partes

obtenerPartesURL("navegacion.csv",5)