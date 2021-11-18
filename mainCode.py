import pandas as pd

def leerdatos(archivo ):
    df=pd.read_csv(archivo)

def separarColumnas(archivo):
    df=pd.read_csv(archivo)
    df.shape