import pandas as pd
import matplotlib.pyplot as plt

estudiantes = {
  'nombres': ["Ana", "Pedro", "Maria", "Ana", "Laura", "Carlos", "Laura", "Carlos", "Valentina", "Pedro", "Valentina", "Maria"],
  'materias': ["Python", "Estadística", "Análisis Matemático","Estadistica", "Estadística", "Análisis Matemático","Python", "Estadística", "Análisis Matemático","Python", "Estadística", "Python"],
  'notas' : [2.5,3.2,3,2.5,4.3,3.6,3.8,2.2,4.6,4.7,2.9,3.8]
}

df = pd.DataFrame(estudiantes)
#muestra la media de las ntoas
dfp = df.groupby(['nombres'])['notas'].mean()
#index false para que no aparesca los indices
df.to_excel('estudiantes.xlsx', index=False)
dfp.to_excel('promedio.xlsx', index=False)
#generar csv
df.to_csv('estudiantes.csv', index=False)
dfp.to_csv('promedio.csv', index=False)
#generar json
df.to_json('estudiantes.json', index=False)
dfp.to_json('promedio.json', index=False)

#graficar dataframprocesado
#dfp.plot(kind='pie', subplots=True)
dfp.plot(kind='pie', autopct='%1.0f%%', subplots=True)
plt.show()
