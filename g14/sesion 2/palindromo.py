# palabra palindromo - se escriben de la misma forma al derecho y al reves

# Función para verificar si una palabra es un palíndromo
def es_palindromo(palabra):
    # Convertir la palabra a minúsculas y quitar espacios
    palabra = palabra.replace(" ", "").lower()
    # Comparar la palabra con su versión invertida
    if palabra == palabra[::-1]:
        return True
    else:
        return False

# Solicitar una palabra al usuario
palabra = input("Introduce una palabra o frase: ")

# Verificar si es palíndromo
if es_palindromo(palabra):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")