#Area de un triangulo

#se define funcion para obtener base y altura
def area_triangulo(base, altura):
  #realizamos la operacion matematica para hallar el area
  area = (base*altura) / 2
  #Devolvemos el valor del area calculado
  return area

# Pedimos al usuario que ingrese la base y la altura
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

#guardamos en una variable el calculo que se realiza en la funcion
resultado = area_triangulo(base, altura)

#imprimimos el resultado
# Imprimimos el resultado
print("El área del triángulo es:", resultado)