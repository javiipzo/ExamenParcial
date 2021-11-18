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
