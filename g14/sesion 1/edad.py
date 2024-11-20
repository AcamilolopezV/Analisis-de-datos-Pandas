#Adulto o jovem

# Solicitar nombre y edad
nombre = input("Introduce el Nombre: ")
edad = int(input("Introduce la Edad: "))

if edad >= 18:
  print(f"{nombre} es Adulto")
else:
  print(f"{nombre} es Joven")