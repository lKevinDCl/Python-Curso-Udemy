import os

'''
## Esto me trae mi ruta actual
#ruta = os.getcwd()

## Permite establecer una ruta en el directorio distinta
ruta = os.chdir('C:\\Users\\kevin\\OneDrive\\Escritorio')

## O podemos generar una carpeta nueva en algun diectorio preestablecido
#ruta = os.makedirs('C:\\Users\\kevin\\OneDrive\\Escritorio\\nueva_carpeta')

archivo = open('archivo_externo.txt')
print(archivo.read())


ruta = 'C:\\Users\\kevin\\PycharmProjects\\pythonProject\\Curse\\Día 6\\prueba.txt'
#elemento = os.path.basename(ruta) esto imprime prueba.txt
#elemento = os.path.dirname(ruta) Esto nos trae solo la ruta sin mostrar el archivo dentro
elemento = os.path.split(ruta) #Si deseamos tener ambos elementos en una tupla, podemos usar el siguiente metodo split
print(elemento)


import os
## Esto elimina las carpetas que hayamos creado
os.rmdir('C:\\Users\\kevin\\OneDrive\\Escritorio\\nueva_carpeta'
'''


#Path permite que las rutas de nnuestros directorios puedas ser abiertos en otros sistemas operativos

from pathlib import Path

carpeta = Path('C:/Users/kevin/OneDrive/Escritorio/nueva_carpeta')
archivo = carpeta / 'archivo_externo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())

