"""def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x * 10)
    return lista

def mi_generador():
    for x in range(1,5):
        yield x * 10

print(mi_funcion())
print(mi_generador())

g = mi_generador()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
"""

def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x+= 1
    yield x


g = mi_generador()

print(next(g))
print(next(g))

print('Hola mundo')

print(next(g))

'Ejercicio 1'

'''
Práctica Generadores 1
Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números, iniciando desde el 1, y entregando un número consecutivo superior cada vez que sea llamada mediante next.

Pista: Utiliza un loop while para realizar este ejercicio.
'''


def mi_generador():
    x = 0
    while True:
        x += 1
        yield x


generador = mi_generador()

'Ejercicio 2'

'''
Práctica Generadores 2
Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida múltiplos de 7, iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).
'''


def mi_generador():
    x = 0
    while True:
        x += 7
        yield x


generador = mi_generador()

'Ejercico 3'

'''
Práctica Generadores 3
Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje cada vez que sea llamado:

"Te quedan 3 vidas"

"Te quedan 2 vidas"

"Te queda 1 vida"

"Game Over"

Almacena el generador en la variable perder_vida
'''


def mi_generador():
    vidas = 3

    while vidas >= 0:

        if vidas > 1:
            yield f'Te quedan {vidas} vidas'
        elif vidas > 0:
            yield f'Te queda {vidas} vida'
        else:
            yield 'Game Over'
        vidas -= 1

perder_vida = mi_generador()

