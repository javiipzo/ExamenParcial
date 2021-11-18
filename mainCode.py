import pandas as pd

def leerdatos(archivo):
    df=pd.read_csv(archivo)
    print(df)

leerdatos("navegacion.csv")