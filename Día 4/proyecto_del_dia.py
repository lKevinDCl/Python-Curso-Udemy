#Crear un Juego

#Se le solicita el nombre al usuario

#maquina: Pensar un numero entre 1 y 100 y usuario tiene 8 intentos

#Dependiendo de la respuesta del usuario la computadora respondera 4 cosas diferentes:
# si el numero no esta entre 1 y 100 "El numero no esta permitido"
# Si el numero es menor al pensado por el programa, este devolvera un mensaje de que el numero es menor
# Si el numero es mayor al pensado por el programa, este devolvera un mensaje de que el numero es mayor
# Si acierta el numero le dira al usuario que ganó y cuantos intentos le tomo

from random import *




print("*****BIENBENIDO A ADIVINAEL NUMERO :D*****")

nombre = input("Cual es tu nombre amiguito?\n")

print(f"\n\nBIENVENIDO {nombre} \nA continuacion pensare en\nun numero del 1 al 100\ny tu deereas \n***ADIVINARLO*** \ntienes 8 intentos\nno te preocupes,\nyo te dire si estas cerca de \nla solución :D")

##La maquina piensa un numero
numero_maquina = randint(1, 100)

intentos = 1
while intentos < 8:

    print(numero_maquina)

    ##Usuario Responde un numero
    numero_jugador = int(input("\n\nDime un numero:\n"))

    match numero_jugador:
        case _ if numero_jugador > 101 or numero_jugador < 0:
            print("Es una broma, ¿verdad? .-.")
        case _ if numero_jugador > numero_maquina and numero_jugador < 101:
            print("El número es menor")
        case _ if numero_jugador < numero_maquina and numero_jugador > 0:
            print("El número es mayor")
        case _ if numero_jugador == numero_maquina:
            print(f"¡Has ACERTADO! Mi número es: {numero_maquina} y lo conseguiste en {intentos} intentos")
            break;
        case _:
            print("Sigue participando :c")
    intentos += 1

print(f"Gracias por Jugar {nombre} :D!")