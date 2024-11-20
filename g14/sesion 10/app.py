import pandas as pd
import matplotlib.pyplot as plt

#Leer archivos de Excel
#1.1)Leer datos desde Excel.
#print('**************************************************')
datos = pd.read_excel('gastos.xlsx')
# #1.2)Consultar estadística inicial de los datos.
# print('**************************************************')
# print(datos.describe())
# #1.3) Consultar los metadatos.
# print('**************************************************')
# print(datos.info())
# #1.4) Consultar tamaño del set de datos. filas y columnas
# print('**************************************************')
# print(datos.shape)
# #1.5) Consultar columnas del set de datos.
print('**************************************************')
print(datos.columns)

#Limpiar datos
#2.1. Consultar valores nulos.
#print('**************************************************')
#print(datos[datos['Valor'].isna()])
#2.2. Borrar valores nulos.
#print('**************************************************')
#datos.dropna(inplace=True)
#print(datos[datos['Valor'].isna()])
#2.3. Consultar valores duplicados
# print('**************************************************')
# print(datos[datos.duplicated()])
#2.4. Borrar datos repetidos.
#print('**************************************************')
datos.drop_duplicates(inplace=True)
#2.5. Remplazar valores de categorías
print('**************************************************')
# print(datos)
# datos.replace({'Servicios':'Servicios Publicos','Luz':'Luz ESSA'}, inplace=True)
# print(datos)
print(datos['Categoría'].unique())
print(datos['Clase de Gasto'].unique())
print(datos['Tipo'].unique())
print(datos['Prioridad'].unique())
#2.6. Borrar espacios en blanco en datos
print('**************************************************')
print(datos)
datos['Categoría'] = datos['Categoría'].str.strip()
print(datos) 
#2.7. Combinar columnas.
print('**************************************************')
datos['Valor * 2'] = datos['Valor']*2
datos['Clase y gasto'] = datos['Clase de Gasto'].str.cat(datos['Prioridad'], sep=' ')
print(datos)
print(datos.info())
#2.8. Borrar columnas.
print('**************************************************')
datos.drop(['Clase y gasto'], axis=1, inplace=True) 
print(datos)
#2.9. Identificar valores Outliers.
datos.plot(kind='box')
plt.show()
