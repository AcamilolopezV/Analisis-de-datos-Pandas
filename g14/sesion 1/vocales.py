#Vocales

# Definir las vocales abiertas y cerradas en dos listas
vocales_abiertas = ['a', 'e', 'o']
vocales_cerradas = ['i', 'u']

# Leer la vocal desde el teclado y la convierte en minuscula
vocal = input("Introduce una vocal: ").lower()

# Comprobar si es una vocal abierta o cerrada
if vocal in vocales_abiertas:
    print(f"La vocal '{vocal}' es una vocal abierta.")
elif vocal in vocales_cerradas:
    print(f"La vocal '{vocal}' es una vocal cerrada.")
else:
    print("No has introducido una vocal válida.")
