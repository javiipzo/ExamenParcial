import pandas as pd
from pandas.core.frame import DataFrame
import urllib
import urllib3
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

#obbtener todas las partes de la url, issue2
def obtenerPartesURL(archivo,columna):
    df=pd.read_csv(archivo, sep=";")
    #primero obtengo la URL
    df.iloc[columna]
    partes = urllib.parse.split("&")

obtenerPartesURL("navegacion.csv","Column 6")