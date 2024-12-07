from pathlib import  Path
'''
base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona","Sagrada_Familia"))

guia2 = guia.with_name('La_predera')#Esto puede reutilizar la ruta pero cambiando el archivo de destino

print(guia)
print(guia2)

'''

guia = Path (Path.home(), "Europa")

# **/*.txt Permite traer todos los archivos .txt del directorio sin importar las subcarpetas
# *.txt Permite traer todos los archivos tx exclusivamente de una carpeta.
for txt in Path(guia).glob("**/*.txt"):
    print(txt)

'Ejercicio 1'

from pathlib import Path

ruta_base = Path.home()

'Ejercicio 2'
from pathlib import Path

ruta = Path("Curso Python","Día 6", "practicas_path.py")

'Ejercicio 3'

from pathlib import Path

base = Path.home()

ruta = Path(base, "Curso Python", "Día 6", "practicas_path.py")