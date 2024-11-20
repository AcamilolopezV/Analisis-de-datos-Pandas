#Año bisiesto

# Leer el año por teclado
año = int(input("Introduce un año: "))

# Comprobar si es bisiesto
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
