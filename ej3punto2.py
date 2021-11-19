import pandas as pd
def leerdatos(archivo):
    return pd.read_csv(archivo, sep = ';')

def mostrar_datos(archivo):
    print(archivo)
navegacion = leerdatos('navegacion.csv')
conversion = leerdatos('conversiones.csv')
#print(navegacion.head())
Df = navegacion['url_landing'].str.split('&', expand = True)
#print(Df.head())
Df.columns = ['url_landing','idUser', 'uuid', 'camp', 'adg', 'device', 'sl', 'adv', 'rec', 'vacía']
id=Df.shape['id_user']
gclid = Df.shape['gclid']
user_recurrent = Df.shape['user_recurrent']
for i in range (id):
    if id == None:
        gclid
        for i in range (gclid):
            if gclid == None:
                user_recurrent
print(i)




