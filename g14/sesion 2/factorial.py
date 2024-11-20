#factorial

# Leer un número por teclado
numero = int(input("Introduce un número: "))

# Inicializar la variable factorial
factorial = 1

# Comprobar si el número es negativo, cero o positivo
if numero < 0:
    print("El factorial no está definido para números negativos.")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    # recorrer el numero y multiplicarlo
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es {factorial}.")
