#factorial

# Inicializar los primeros dos números de la serie de Fibonacci
a, b = 0, 1

# Imprimir la serie de Fibonacci hasta 500
print("Serie de Fibonacci hasta 500:")
while a <= 500:
    print(a, end=", ")
    a, b = b, a + b
