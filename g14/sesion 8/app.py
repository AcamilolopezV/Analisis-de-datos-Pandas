import pandas as pd

estudiantes = {
  'nombres': ["Ana", "Pedro", "Maria", "Ana", "Laura", "Carlos", "Laura", "Carlos", "Valentina", "Pedro", "Valentina", "Maria"],
  'materias': ["Python", "Estadística", "Análisis Matemático","Estadistica", "Estadística", "Análisis Matemático","Python", "Estadística", "Análisis Matemático","Python", "Estadística", "Python"],
  'notas' : [2.5,3.2,3,2.5,4.3,3.6,3.8,2.2,4.6,4.7,2.9,3.8]
}

#listar datos del diccionario en dataframe
df = pd.DataFrame(estudiantes)
print(df)
print()
#2) mostrar los datos de una columna (notas)
print('#2) mostrar los datos de una columna')
print(df['notas'])
print()
#3) Cambiar el encabezado de una columna (materias)
print('#3) Cambiar el encabezado de una columna (materias)')
df = df.rename(columns={'materias': 'asignaturas'})
print(df)
print()
#4) Mostrar el primer registro
print('#4) Mostrar el primer registro')
print(df.head(1))
print()
#5) Mostrar el ultimo registro
print('#5) Mostrar el ultimo registro')
print(df.tail(1))
print()
#6) mostrar los primeros 5 registros
print('#6) mostrar los primeros 5 registros')
print(df.head(5))
print()
#7) mostrar los primeros 2 primeros registros
print('#7) mostrar los primeros 2 primeros registros')
print(df.head(2))
#8) Mostrar los ultimos 5 resgistros
print('#8) Mostrar los ultimos 5 resgistros')
print(df.tail(5))
print()
#9) Filtrar por los estudiantes con notas mayores a 3
print('#9) Filtrar por los estudiantes con notas mayores a 3')
df_mayorTres = df[df['notas'] > 3]
print(df_mayorTres)
print()
#10) Filtrar por los estudiantes con notas mayores a 4.5
print('#9) Filtrar por los estudiantes con notas mayores a 4.5')
df_mayorCuatro= df[df['notas'] > 4.5]
print(df_mayorCuatro)
print()
#11) sacar la maxima nota
print('#11) sacar la maxima nota')
nota_maxima = df['notas'].max()
print(nota_maxima)
print()
#12) sacar la minima nota
print('#12) sacar la minima nota')
nota_minima = df['notas'].min()
print(nota_minima)
print()
#13) sacar los estudiantes que van ganando el año
#mena para sacar el promedio de dato de notas en este caso y se agrupa por nombre
print('#13) sacar los estudiantes que van ganando el año - nota minima 3')
df = pd.DataFrame(estudiantes)
dfp = df.groupby(['nombres'])['notas'].mean().reset_index()
print(dfp[dfp['notas']>=3])
print()
#14) sacar los etudiantes que van perdiendo el año
print('#14) sacar los estudiantes que van perdiendo el año')
print(dfp[dfp['notas']<3])
print()
#15) sacar el mejor estudiante
print('#15) sacar el mejor estudiante')
print(dfp[dfp['notas'] == dfp['notas'].max()])
print()
#16) sacar el peor estudiante
print('#16) sacar el peor estudiante')
print(dfp[dfp['notas'] == dfp['notas'].min()])
print()
#17) Sacar la media
print('#17) Sacar la media')
print(df['notas'].mean())
print()
#18) sacar la mediana
print('#18) sacar la mediana')
print(df['notas'].median())
print()
#19) sacar la moda
print('#19 sacar la moda')
print(df['notas'].mode())
print()
#20) sacar la desviacion estandar
print('#20) sacar la desviacion estandar')
print(f"{(df['notas'].std()):.3f}")
print()
#21) mostrar el numero de registros de un dataframe
print('#21) mostrar el numero de registros de un dataframe')
df = pd.DataFrame(estudiantes)
num_filas = df.count()
print(num_filas)
print()
#22) mostrar el tamaño de los datos de un dataframe numero de filas y columnas
print('#22) mostrar el tamaño de los datos de un dataframe numero de filas y columnas')
print(df.shape)
print()
#filas y columnas
#23) Agrupar los datos por nombre del estudiante
print('#23) Agrupar los datos por nombre del estudiante')
print(df.groupby(['nombres'])['notas'].mean())
print()
#24)Ordenar los datos por nombre de materias
print('#24)Ordenar los datos por nombre de materias')
print(df.groupby(['materias'])['notas'].mean())
#24)Filtrar los datos por nombre del estudiante.
print('#24)Filtrar los datos por nombre del estudiante.')
print(df.sort_values("nombres", ascending=True))
print()
#25) buscar por nombre
nombre = input("Estudiante a buscar: ")
print(df[df['nombres'] == nombre])

























