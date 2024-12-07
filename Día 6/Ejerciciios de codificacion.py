'''from pathlib import Path


def abrir_leer(direccion):
    archivo = Path(direccion)

    return archivo.read_text()
'''


'''
from pathlib import Path

def sobrescribir(directorio):
    archivo = Path(directorio)

    return archivo.write_text("contenido eliminado")
'''

from pathlib import Path

def registro_error(directorio):
    archivo = Path(directorio)

    archivo.open('a').write("se ha registrado un error de ejecución")

    return archivo