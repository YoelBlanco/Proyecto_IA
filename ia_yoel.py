
#Luego, podemos proceder a escribir el código que lea el archivo Excel y analice los datos. Aquí te dejo un ejemplo de cómo podrías hacerlo:

#El código anterior lee un archivo Excel de la ruta especificada y utiliza la función "obtener_productos_mas_vendidos" para obtener los productos más vendidos. Esta función toma el DataFrame leído y el número de productos que quieres obtener. Luego, agrupa los productos por nombre y los ordena según la cantidad de días  entrada en orden descendiente. Toma los n productos más vendidos y calcula el promedio diario de entrada para cada uno. Para mostrar los resultados en una interfaz gráfica, podemos utilizar la librería tkinter en Python. Aquí te dejo un ejemplo de cómo podrías hacerlo:

import tkinter as tk
import pandas as pd
import openpyxl 

# Función para leer los datos del archivo Excel
def leer_excel(ruta_archivo):
    # Lee el archivo Excel y lo convierte en un DataFrame de pandas
    df = pd.read_excel(ruta_archivo, engine='openpyxl')
    return df

# Función para obtener los productos más vendidos
def obtener_productos_mas_vendidos(df, num_productos):
    # Agrupa los productos por nombre y suma la cantidad de días entrada
    agrupados = df.groupby('Nombre del Producto')['días de entrada'].sum().reset_index()
    # Ordena los productos por cantidad de días entrada en orden descendiente
    ordenados = agrupados.sort_values(by=['días de entrada'], ascending=False)
    # Toma los n productos más vendidos
    mas_vendidos = ordenados.iloc[:num_productos]
    # Calcula el promedio diario para cada producto
    mas_vendidos['promedio diario'] = mas_vendidos['días de entrada'] / num_productos
    return mas_vendidos

# Función para mostrar los resultados en una ventana
def mostrar_resultados(ruta_archivo, num_productos):
    df = leer_excel(ruta_archivo)
    mas_vendidos = obtener_productos_mas_vendidos(df, num_productos)
    
    # Crear ventana para mostrar los resultados
    ventana_resultados = tk.Toplevel()
    
    # Crear tabla en la ventana para mostrar los resultados
    tabla = tk.Text(ventana_resultados)
    tabla.pack()
    
    # Imprimir los resultados en la tabla
    tabla.insert(tk.END, "Nombre del Producto\tDías de Entrada\tPromedio Diario\n")
    for index, row in mas_vendidos.iterrows():
        tabla.insert(tk.END, f"{row['Nombre del Producto']}\t\t\t{row['días de entrada']}\t\t\t{row['promedio diario']:.2f}\n")

# Crear ventana principal
ventana_principal = tk.Tk()

# Crear botón para seleccionar archivo
btn_seleccionar_archivo = tk.Button(ventana_principal, text="Seleccionar archivo")
btn_seleccionar_archivo.pack()

# Crear campo de texto para ingresar número de productos
entry_num_productos = tk.Entry(ventana_principal)
entry_num_productos.pack()

# Crear botón para ejecutar análisis
btn_analizar = tk.Button(ventana_principal, text="Analizar")
btn_analizar.pack()

# Conectar botón de selección de archivo con función de selección de archivo
btn_seleccionar_archivo.config(command=lambda: mostrar_resultados("Datos.xlsx", int(entry_num_productos.get())))

# Iniciar bucle principal de la ventana
ventana_principal.mainloop()