import pandas as pd
from pandas.core.frame import DataFrame
import urllib
def leerdatos(archivo ):
    df = pd.read_csv(archivo)
    return df

def getvalue(archivo,fila,dato):
    df = pd.read_csv(archivo)
    df._get_value(fila,dato)

def separarColumnas(archivo):
    df=pd.read_csv("archivo", sep=";")
leerdatos("navegacion.csv")

def obtenerPartesURL(archivo,columna):
    df=pd.read_csv(archivo)
    #primero obtengo la URL
    DataFrame.iloc[columna]
    partes = urllib.parse.split("&")

obtenerPartesURL("navegacion.csv","url_landing")