import pandas as pd

def leer_excel(ruta_archivo):
    # Lee el archivo Excel y lo convierte en un DataFrame de pandas
    df = pd.read_excel(ruta_archivo, engine='openpyxl')
    return df
    
df = leer_excel("D:/Universidad/4to SEM_1/IA/Ultimo Proyecto/Datos.xlsx")
for index, row in df.iterrows():
    print(row)