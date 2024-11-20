import pandas as pd
import matplotlib.pyplot as plt

#Leer datos
datos = pd.read_excel('gastos.xlsx')
print('**************************************************')
print(datos.columns)
# 2.1. Asignar tipo fecha
print('**************************************************')
datos['Fecha'] = pd.to_datetime(datos['Fecha'])
print(datos['Fecha'])
# 2.2. Buscar por rango de fechas
print('**************************************************')
dff = datos[datos['Fecha'].between('2024-01-01','2024-02-25')]
print(dff)
# 2.3. Buscar por año
#print('**************************************************')
#dy = datos[datos['Fecha'].dt.year == 2024]
#Otra forma de realizarlo
dy = datos[datos['Fecha'].dt.year.isin([2024])]
print(dy)
# 2.4. Agregar columna de mes
print('**************************************************')
datos['mes_abreviado'] = datos['Fecha'].dt.strftime('%B')
print(datos['mes_abreviado'])
# 2.5. Asignar día del año
print('**************************************************')
datos['dia'] = datos['Fecha'].dt.day_name()
print([datos['dia']])
# 2.6. Agrupar por mes
print('**************************************************')
datos = datos.dropna(subset=['Fecha'])
datos['Mes'] = datos['Fecha'].apply(lambda x:x.strftime('%B'))
#print(['Mes'])
datos['Nmes'] = datos['Fecha'].dt.month
dff = datos.groupby(['Nmes','Mes','Categoría'])['Valor'].sum().unstack()
colors = ['red','IndianRed','orange','yellow','purple','pink']
#dff.plot.bar(color=colors)
#plt.show()
# 3.1. Graficar en Barra serie en días del año
datos['Fecha'] = pd.to_datetime(datos['Fecha'])
datos.set_index('Fecha', inplace=True)
#crear grafico
plt.figure(figsize=(12, 6))
datos.plot(kind='bar')
plt.title('Gráfico de barras diario')
plt.xlabel('Día del año')
plt.ylabel('Valor')
plt.show()
