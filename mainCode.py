import pandas as pd

def leerdatos(archivo ):
    df=pd.read_csv(archivo)
    print(df)
def separarColumnas():
    df1=pd.read_csv("conversiones.csv")
    df1.shape
    listaConversiones = []
    for i in range(df1.shape[0]):
        valores = df1._get_value(i, "camp;adg;sl;adv")
        listaConversiones.append(valores.split(";"))
    df2=pd.read_csv("navegacion.csv")
    df2.shape
    listaNavegación = []
    for i in range(df2.shape[0]):
        valores = df2._get_value(i, "camp;adg;sl;adv")
        listaNavegación.append(valores.split(";"))