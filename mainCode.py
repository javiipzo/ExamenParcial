import urllib
import pandas as pd
from pandas.core.frame import DataFrame
from urllib import parse

def leerdatos(archivo ):
    df=pd.read_csv(archivo)
    print(df)

def getvalue(archivo,fila,dato):
    df=pd.read_csv(archivo)
    df._get_value(fila,dato)

def separarColumnas(archivo):
    df=pd.read_csv("archivo", sep=";")
leerdatos("navegacion.csv")

def obtenerPartesURL(archivo):
    df=pd.read_csv(archivo)
    #primero obtengo la URL
    DataFrame.iloc["url_landing"]
    partes = urllib.parse.split("&")
    for parte in partes:

