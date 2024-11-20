#Dias de la semana

#funcion para calcular el dia de la semana segun el numero ingresado 
def obtener_dia_semana(numero):
  #se guarda en una lista los dias de la semana
  dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
  if 1 <= numero <= 7:
    return dias_semana[numero - 1]
  else:
    return "Número inválido. Ingrese un número entre 1 y 7."

# Pedimos al usuario que ingrese un número
numero = int(input("Ingrese un número del 1 al 7 para obtener el día de la semana: "))

# Obtenemos el día de la semana correspondiente
dia = obtener_dia_semana(numero)

# Imprimimos el resultado
print(dia)
