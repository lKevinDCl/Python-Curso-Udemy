#   Ejercicio udemy
def suma(*args):

    total = 0

    for arg in args:
        total += arg

    return total

print(suma(5,6,5))

'''

Práctica sobre Argumentos Indefinidos (*args) 1
Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.



Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).
'''

def suma_cuadrados(*args):
    total = 0

    for arg in args:
        total += arg**2

    return total

'''
Práctica sobre Argumentos Indefinidos (*args) 2
Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).
'''

def suma_absolutos(*args):
    total = 0
    for arg in args:
         total += abs(arg)

    return total

'''
Práctica sobre Argumentos Indefinidos (*args) 3
Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}"
'''

def numeros_persona(nombre, *args):
    suma_numeros = 0
    for arg in args:
        suma_numeros += arg

    return f"{nombre}, la suma de tus números es {suma_numeros}"