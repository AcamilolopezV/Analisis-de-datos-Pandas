#Hipotenusa
import math

#se define funcion para hallar la hipotenusa de un triangulo
def calcular_hipotenusa(cateto1, cateto2):
  #se realizan los calculos para hallar hipotenusa segun formula
  hipotenusa_cuadrado = cateto1**2 + cateto2**2
  hipotenusa = math.sqrt(hipotenusa_cuadrado)
  #me devuelve el resultado de la uperacion guardada en hipotenusa
  return hipotenusa

# Pedimos al usuario que ingrese los catetos
cateto1 = float(input("Ingrese la longitud del primer cateto: "))
cateto2 = float(input("Ingrese la longitud del segundo cateto: "))

# Calculamos la hipotenusa
resultado = calcular_hipotenusa(cateto1, cateto2)

# Imprimimos el resultado
print("La hipotenusa del triángulo es:", resultado)