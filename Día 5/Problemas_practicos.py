# Ejercicio 1
def devolver_distintos(*args):

    total = 0
    lista = list(args)

    for arg in args:
        total += arg

    if total > 15:
        return max(args)
    elif total < 10:
        return min(args)
    else:
        #return (max(args) + min(args)) /2
        #return total / len(args)
        lista.sort()
        return lista[1]


print(devolver_distintos(7,2,4))

# Ejercicio 2
def separador_palabra(palabra):

    #lista = list(palabra.lower())
    #lista.sort()

    mi_set = set()
    for letra in palabra:
        mi_set.add(letra)

    mi_lista = list(mi_set)
    mi_lista.sort()

    return mi_lista


print(separador_palabra('Hola mundo'))

# Ejercicio 3
def cero_repetido(*arg):

    mi_lista = list(arg)
    contador = 0

    for numero in mi_lista:

        if numero == 0:
            contador += 1
            if contador == 2:
                return True
        else:
            contador = 0
    return False

print(cero_repetido(5,6,1,0,0,9,3,5))
print(cero_repetido(6,0,5,1,0,3,0,1))

# Ejercicio 4
def contar_primos(numero):

    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0

    while iteracion <= numero:

        for n in range(3, iteracion,2):

            if iteracion % n == 0:
                iteracion += 2
                break
        else:
                primos.append(iteracion)
                iteracion += 2

    print(primos)
    return len(primos)

print(contar_primos(9))