# To do in class
import random

respuesta = random.randint(1, 1001)

intento = int(input("Ingresa un numero entre 1 y 1000: "))

numero_intentos = 10

# Main loop
while (numero_intentos != 0):
    if (respuesta == intento):
        print("Ganaste")
        break
    elif (intento > respuesta):
        print("La respuesta que buscas es menor")
        numero_intentos -= 1
        print("Intentos restantes: " + str(numero_intentos))
    elif (intento < respuesta):
        print("La respuesta que buscas es mayor")
        numero_intentos -= 1
        print("Intentos restantes: " + str(numero_intentos))
    intento = int(input("Ingresa un numero entre 1 y 1000: "))

if (numero_intentos == 0):
    print("Perdiste, la respuesta era: " + str(respuesta))