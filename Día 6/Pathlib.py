from pathlib import Path, PureWindowsPath


#Con pathlib nos permite hacer lo mismo que antes pero sin la necesidad de abrir o cerrar los archivos
carpeta = Path('C:/Users/kevin/PycharmProjects/pythonProject/Curse/Día 6/prueba.txt')

ruta_windows = PureWindowsPath(carpeta) #Nos permite convertir una ruta en una ruta windows
#print (carpeta.read_text()) permite leer el contenido del archivo
#print (carpeta.name) Nos da el nombre del archivo
#print (carpeta.suffix) nos devuelve el sufijo es decir .txt
#print (carpeta.stem) nos da el nombre del archivo sin el sufijo
print (carpeta.write_text())


print(ruta_windows)

if not carpeta.exists():
    print("Este archivo no exioste")
else:
    print("Genial, existe")
