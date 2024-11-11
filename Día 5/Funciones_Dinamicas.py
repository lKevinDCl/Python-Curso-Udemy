#Ejemplo del video
'''
def chequear_3_cifras(numero):
    return  numero in range(100, 1000)

#suma = 568 + 402

resultado = chequear_3_cifras(suma)

print(resultado)
'''

def chequear_3_cifras (lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras
resultado = chequear_3_cifras([555,99,600])

print(resultado)

##Ejecicios Udemy

'''
Práctica Funciones Dinámicas 1
Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.

No invoques la función, solo es necesario definirla.
'''

def todos_positivos(lista):

    for n in lista:
        if n < 0:
            return False
        else:
            pass
    return True

#lista_numeros = [12,-5,10,-10]

#print(todos_positivos(lista_numeros))

'''
Práctica Funciones Dinámicas 2
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.

'''
def suma_menores(lista):
    suma = 0

    for n in lista:
        if n > 0 and n < 1000:
            suma += n
        else:
            pass
    return suma

lista_numeros = [1,2,3,4,5,6,7,8,9]

print(suma_menores(lista_numeros))

'''

Práctica Funciones Dinámicas 3
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.
'''


def cantidad_pares(lista):

    contador = 0

    for n in lista:

        if n % 2==0:
            contador += 1
        else:
            pass
    return  contador

lista_numeros = [1,2,3,4,5,6,7,8,9]
cantidad_pares(lista_numeros)



