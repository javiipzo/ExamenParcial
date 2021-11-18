import pandas as pd
from pandas.core.frame import DataFrame

def leerdatos(archivo ):
    df=pd.read_csv(archivo)
    df

def separarColumnas(archivo):
    df=pd.read_csv(archivo)
    df.shape
    lista = []
    for i in range(df.shape[0]):
        valores = df._get_value(i, "camp;adg;sl;adv")
        lista.append(valores.split(";"))
