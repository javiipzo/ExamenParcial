import pandas as pd
def leerdatos(archivo):
    return pd.read_csv(archivo, sep = ';')

def mostrar_datos(archivo):
    print(archivo)
navegacion = leerdatos('navegacion.csv')
conversion = leerdatos('conversiones.csv')
print(navegacion.head())
Df = navegacion['url_landing'].str.split('&', expand = True)
print(Df.head())
Df.columns = ['url_landing','idUser', 'uuid', 'camp', 'adg', 'device', 'sl', 'adv', 'rec', 'vacía']
if navegacion['id_user'] == None:
    navegacion['gclid']
    if navegacion['gclid'] == None:
        navegacion['user_recurrent']





