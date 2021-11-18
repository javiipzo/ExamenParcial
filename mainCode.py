import pandas as pd

def leerdatos(archivo ):
    df=pd.read_csv(archivo)
    print(df)
    

def separarColumnas(archivo):
    df=pd.read_csv(archivo)
    df.shape
    lista = []
    for i in range(df.shape[0]):
        valores = df._get_value(i, "date;hour;id_lead;id_user;gclid;lead_type;result")
        lista.append(valores.split(";"))