#20numeros y guardarlos 

# Crear una lista vacía para almacenar los 20 números
numeros = []

# Leer 20 números por teclado
for i in range(20):
    #recorre 20 veces 
    numero = int(input(f"Introduce el número {i+1}: "))
    #se agregan con append a la lista numero
    numeros.append(numero)

# Imprimir los números antes de ordenar
print("\nNúmeros ingresados:")
print(numeros)

# sort Ordena los números en orden descendente con el parametro reverse = true por que por defecto ordena ascendente
numeros.sort(reverse=True)

# Imprimir los números ordenados
print("\nNúmeros ordenados descendentemente:")
print(numeros)
