# Función para comprobar si un número es primo
def es_primo(num):
  #ningun numero menor que 2 es considerado primo
    if num < 2:
      #retorna falso 
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Imprimir los primeros 100 números primos
contador = 0
numero = 2
#recorre hasta 100
while contador < 100:
  # se empieza desde 2 a validar si es primo y se incrementa de a 1
    if es_primo(numero):
        print(numero)
        contador += 1
    numero += 1
