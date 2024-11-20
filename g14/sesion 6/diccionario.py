import pandas as pd 

estudiantes = {
  'nombre' : ["Camio","Alberto","Jose","Isabela","Andres"],
  'materia' : ["Python","Estadistica","Matematicas","HTML","CSS"],
  'asistencia' :[1,1,1,2,3],
  'nota' : [4.5,3.2,4.4,3.2,4.1]
}

df = pd.DataFrame(estudiantes)
print(df)
print(df.describe())
#Guardar el dataFrame en un archivo
df.to_excel('estudiantes.xlsx', index=False)