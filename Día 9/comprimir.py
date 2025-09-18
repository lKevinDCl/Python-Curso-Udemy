import zipfile

"""mi_zip = zipfile.ZipFile('archivo_comporimido.zip', 'w')

mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()"""

zip_abierto = zipfile.ZipFile('archivo_comporimido.zip', 'r')

zip_abierto.extractall()



import shutil

carpeta_origen = 'C:\\Users\\Kevin\\Documents\\Carpeta_Superior'

archivo_destino = 'Todo_Comprimido'

shutil.make_archive(archivo_destino, 'zip', carpeta_origen)




shutil.unpack_archive('Todo_Comprimido.zip', 'Extraccion Terminada','zip')
