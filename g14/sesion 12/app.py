import pandas as pd
import matplotlib.pyplot as plt

#Leer datos
datos = pd.read_excel('gastos.xlsx')
print('**************************************************')
print(datos.columns)
# 1.1. Agrupar total de ingresos y gastos.
print('************************************************')
total = datos.groupby(['Clase'])['Valor'].sum().sort_values()
print(total)
# 1.2. Graficar en pie los datos agrupados de ingresos y Gastos.
# total.plot(kind='pie')
# plt.show()
# 1.3. Separar Ingresos en un dataframe con el nombre de ingresos.
print('************************************************')
ingresos = datos[datos['Clase']=='Ingreso']
salario = datos[datos['Categoría'].isin(['Sueldo'])]
print(ingresos)
print('************************************************')
print(salario)
# 1.4. Separar gastos en un dataframe de gastos.
print('************************************************')
gastos = datos[datos['Clase']=='Gasto']
print(gastos)
# 1.5. Agrupar gastos por categorías.
print('************************************************')
datos['Categoría'] = datos['Categoría'].str.strip()#quitar espacios en blanco de las categorias para que coincidan
total_gastos_categoria = datos.groupby(['Categoría'])['Valor'].sum().sort_values()
print(total_gastos_categoria)
# 1.6. Identificar las categorías de mayor gasto.
print('************************************************')
gastos = datos[datos['Clase'].isin(['Gasto'])]
print(gastos)
gastopc = gastos.groupby(['Categoría'])['Valor'].sum().sort_values(ascending=False)
print(gastopc)
# 1.7. Graficar las categorías en grafico de bar.
#print('************************************************')
# gastopc.plot(kind='bar')
# plt.show()
# 1.8. Identificar las categoría que se pueden convertir en ahorros de dinero.
print('************************************************')
gastopc = gastos.groupby(['Categoría'])['Valor'].sum().sort_values()
print(gastopc)
colors = ['red','IndianRed','orange','yellow','purple','pink']
gastopc.plot(kind='barh', color=colors)
#plt.grid()
plt.show()
