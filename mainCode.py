import pandas as pd

def leerdatos(archivo ):
    df=pd.read_csv(archivo)
    print(df)
    

def separarColumnas(archivo):
    df=pd.read_csv(archivo)
    df.shape
    lista = []
    for i in range(df.shape[0]):
        valores = df._get_value(i, "camp;adg;sl;adv")
        lista.append(valores.split(";"))