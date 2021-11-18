import pandas as pd

def leerdatos(archivo ):
    df=pd.read_csv(archivo)
    print(df)
    

def separarColumnas(archivo):
    df=pd.read_csv(archivo)
    df.shape