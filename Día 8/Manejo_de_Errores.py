def suma():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar")

try:
    # Código que queremos probar
    suma()
except TypeError:
    # Código a ejecutar si hay un error
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    # Código a ejecutar si hay un error
    print("Estas intentando concatenar tipos distintos")
else:
    # Cóidigo a ejecutar si no hay error
    print("Hiciste todo bien")
finally:
    # Código que se va a ejecutar si o si
    print("Eso fue todo")


'''
try:
    # Código que queremos probar
    suma()
except:
    # Código a ejecutar si hay un error
    print("Algo no salio bien")
else:
    # Cóidigo a ejecutar si no hay error
    print("Hiciste todo bien")
finally:
    # Código que se va a ejecutar si o si
    print("Eso fue todo")
'''

def pedir_numero():

    while True:
        try:
            numero = int(input("Dame un numero"))
        except:
            print("Ese no es un numero")
        else:
            print(f'Ingresaste el numero {numero}')
            break
    print("Gracias")

pedir_numero()


