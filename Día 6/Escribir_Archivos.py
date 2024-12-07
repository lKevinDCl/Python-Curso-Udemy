'''#archivo = open ('prueba.txt', 'w')

#archivo.write('Soy el nuevo texto')

#archivo.close()

''
Para poder actualizar un archivo podemos utilizar W o A

w:
nos permite sobreescribir el archivo que teniamos, eliminando todo lo que habia dentro de el con anterioridad

a:
nos permite agregar al archivo al final texto extra. Es decir que solo actualiza lo que ya tenemos

r:
Solo es para lectura como lo dice su sigla en inglés R de Read
''

archivo = open ('prueba.txt', 'a')


archivo.write('\nNueva actualización')
archivo.close()


'Practica 1'
archivo = open('mi_archivo.txt', 'w')

archivo.write('Nuevo texto')

archivo.close()

archivo = open('mi_archivo.txt', 'r')

print(archivo.read())

archivo.close()

'Practica 2 '

archivo = open('mi_archivo.txt','a')

archivo.write("Nuevo inicio de sesión")

archivo.close()

archivo = open('mi_archivo.txt','r')

print(archivo.read())

archivo.close()
'''

'Practica 3'

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

registro = open('registro.txt', 'a')

for l in registro_ultima_sesion:
    registro.writelines(l + '\t')

registro.close()

registro = open('registro.txt', 'r')

print(registro.read())

registro.close()