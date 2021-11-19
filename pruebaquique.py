import re
import pandas as pd
from pandas.core.frame import DataFrame
import urllib

def leerdatos(archivo):
    return pd.read_csv(archivo, sep = ';')

def mostrar_datos(archivo):
    print(archivo)

navegacion = leerdatos('navegacion.csv')
conversion = leerdatos('conversiones.csv')
print(navegacion.head())
Df = navegacion['url_landing'].str.split('&', expand = True)
print(Df.head())
new_df = pd.DataFrame(Df, columns = ['url_landing','idUser', 'uuid', 'camp', 'adg', 'device', 'sl', 'adv', 'rec'])
print(new_df)
