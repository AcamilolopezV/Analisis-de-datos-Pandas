#Masa corporal

# Solicitar peso y estatura por teclado
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

# Calcular el Índice de Masa Corporal (IMC)
indice_masa = peso / (altura ** 2)

# Imprimir el valor del indice de masa con dos decimales
print(f"Tu Índice de Masa Corporal (IMC) es: {indice_masa}")

# Condicional para valida el indice de masa 
if indice_masa < 18.5:
    print("Estás bajo de peso.")
elif 18.5 <= indice_masa < 24.9:
    print("Tienes un peso normal.")
elif 25 <= indice_masa < 29.9:
    print("Estás en sobrepeso.")
else:
    print("Estás obeso.")
