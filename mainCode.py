import re
import pandas as pd

def leerdatos(archivo):
    df=pd.read_csv(archivo)

leerdatos("navegacion.csv")