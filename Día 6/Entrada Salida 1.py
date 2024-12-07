''' ## La variable aloja dentro de si to.do el contenido del archivo
mi_archivo = open('prueba.txt')

## Se puede generar una variable que solo alaje la primera linea del archivo
una_linea = mi_archivo.readline()
## Y imprimimos la primera linea
print(una_linea)


## se pueden imprimir el resto de lineas de la siguiente manera:
## Linea 1
una_linea = mi_archivo.readline()
# Para hacer que una linea no tenga un salto de linea se puee utilizar el metodo rstrip:
print(una_linea.rstrip())

## Linea 2
una_linea = mi_archivo.readline()
print(una_linea)

## Esta linea solo permite ver las caracteristicas del archivo que estamos declarando en la parte superior
#print(mi_archivo)


## el metdo read permite ver el contenido del archivo
print(mi_archivo.read())

## Se recomienda que al termino de la utilizacion de un archivo
## se debe cerrar el archivo para ahorro de memoria
mi_archivo.close()
'''

## A si mismo se puede Iterar
'''
mi_archivo = open('prueba.txt')
for l in mi_archivo:
    print ("'Aqui dice" + l)
'''

## Tambien se puede manejar a manera de listas

mi_archivo = open('prueba.txt')

todas = mi_archivo.readlines()

print(todas)

mi_archivo.close()