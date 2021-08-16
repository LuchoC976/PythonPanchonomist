# Start from scratch after conditionals

print("Elige una opcion: ")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Divison")

opcion = int(input("Opcion: "))

resultado = 0

if (opcion == 1):
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    resultado = num1 + num2
    print("Resultado: " + str(resultado))
elif (opcion == 2):
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    resultado = num1 - num2
    print("Resultado: " + str(resultado))
elif (opcion == 3):
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    resultado = num1 * num2
    print("Resultado: " + str(resultado))
elif (opcion == 4):
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    resultado = num1 / num2
    print("Resultado: " + str(resultado))
else:
    print("Dato invalido")
