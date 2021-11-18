import pandas as pd
from pandas.core.frame import DataFrame

def leerdatos(archivo ):
    df=pd.read_csv(archivo)
    df

def getvalue(archivo,fila,dato):
    df=pd.read_csv(archivo)
    df._get_value(fila,dato)


