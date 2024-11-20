import pandas as pd
import matplotlib.pyplot as plt

#leer excel
datos = pd.read_excel('gastos.xlsx')
print('**************************************************')
print(datos.columns)

#limpieza de los datos
datos.dropna(inplace=True)
datos['Clase'] = datos['Clase'].str.strip()
datos['Tipo'] = datos['Tipo'].str.strip()
datos['Priodidad'] = datos['Prioridad'].str.strip()
datos['Categoría'] = datos['Categoría'].str.strip()

#duplicados
datos.drop_duplicates(inplace=True)
# Limpieza exhaustiva de la columna 'Prioridad'
datos['Prioridad'] = datos['Prioridad'].str.strip()

#graficas procesamiento de datos
print('**************************************************')
gastos = datos[datos['Clase'] == 'Gasto']
categoria = datos[datos['Priodidad']=='Alta']
print(categoria)
total = datos.groupby('Categoría')['Valor'].sum().reset_index()
prioridad = datos.groupby('Prioridad')['Valor'].sum().reset_index()
categoriaP = categoria.groupby('Categoría')['Valor'].sum().reset_index()

plt.subplot(221)
plt.title('Grafica de Lineas')
plt.plot(total['Categoría'],total['Valor'])

plt.subplot(222)
plt.title('Grafica en Barras')
plt.pie(categoriaP['Valor'], labels=categoriaP['Categoría'],autopct='%1.1f%%')

plt.subplot(223)
plt.title('Grafica de Barras')
plt.bar(prioridad['Prioridad'],prioridad['Valor'])

plt.subplot(224)
plt.title('Grafica de Dispersion')
plt.scatter(categoriaP['Categoría'],categoriaP['Valor'])

plt.tight_layout()
plt.show()

