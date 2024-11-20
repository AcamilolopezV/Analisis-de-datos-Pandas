#Numero Mayor

#ingresa los numero a validar 
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

if num1 > num2:
  print(f"El '{num1}' es mayor que el '{num2}'")
elif num2 == num1:
  print(f"El '{num2}' es igual que el '{num1}'")
else:
  print(f"El '{num2}' es mayor que el '{num1}'")
  