import os
import shutil
# import send2trash // Se debe instalar mediante pip install send2trash desde el cmd

'''print(os.getcwd()) #Nos dice la ubicacion actual del archivo 

archivo = open ('curso.txt','w')
archivo.write('texto de prueba')
archivo.close()


print(os.listdir()) #Nos dice cuantos y cuales archivos hay en el directorio
'''

#shutil.move('curso.txt', "C:\\Users\\kevin\\OneDrive\\Escritorio")

#shutil.rmtree elimina la carpeta completa, definitivamente

#send2trash.send2trash('curso.txt') manda los archvos a la papelera evitando que se eliminen de manera definitiva

'''print(os.walk("C:\\Users\\kevin\\documents"))'''

ruta = "C:\\Users\\kevin\\Documents\\Hector" #almacena la ruta

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {ruta}')
    print(f'Las carpetas son:')
    for sub in subcarpeta:

        print(f'\t{sub}')
    print('Los archivos son: ')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')


# El codigo anterior nos permite saber los elementos dentro de las carpetas que se encunetran en la ruta que le especificamos