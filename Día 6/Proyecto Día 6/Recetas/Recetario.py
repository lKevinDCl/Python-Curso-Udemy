from pathlib import Path
from os import system

localizacion_recetas = Path.cwd()

def numero_de_recetas():
    contador = 0

    for txt in Path(localizacion_recetas).glob("**/*.txt"):
        contador += 1

    return contador

def elegir_categoria():
    categorias = []

    for carpeta in localizacion_recetas.iterdir():
        if carpeta.is_dir():
            categorias.append(carpeta.name)

    print(f'Categorias:\n{categorias}\n')

    longitud_carpeta = len(categorias)

    while True:

        op = int(input(f'Seleciona una categoria entre 1 y {longitud_carpeta}\n'))

        if op > 0 and op <= longitud_carpeta:

            return categorias[op-1]
        continue

def elegir_recetas(categoria):
    directorio_local = localizacion_recetas / categoria
    contador = 0
    lista_recetas = []

    for txt in Path(directorio_local).glob("*.txt"):
        contador += 1
        lista_recetas.append(txt.stem)


    print(f'Recetas: \n{lista_recetas}')
    while True:
        op = int(input(f'Seleciona una receta entre 1 y {contador}\n'))

        if op > 0 and op <= contador:
            return lista_recetas[op-1]
        continue

def leer_receta(categoria, receta):
    directorio_local = Path(localizacion_recetas/categoria/receta)
    archivo = directorio_local.with_suffix('.txt')

    contenido = archivo.read_text()

    return print(contenido)

def crear_receta(categoria):

    nombre_receta = input('Dime el nombre de la receta:\n')

    directorio_local = localizacion_recetas/categoria/nombre_receta

    archivo = directorio_local.with_suffix('.txt')

    texto = input('Dame el contenido de la receta:\n')
    archivo.write_text(texto)

    print(f'Archivo creado en:\n{directorio_local}')
    print(f'Nombre del archivo:\n{nombre_receta}')
    print(f'con el siguiente contenido:\n{archivo.read_text()} \n\n')

    return

def crear_categoria():
    nombre_categoria = input('Dime el nombre de la Categoria:\n')

    directorio_local = Path(localizacion_recetas/nombre_categoria)

    directorio_local.mkdir(parents = True, exist_ok=True)

    print(f'categoria creado en:\n{directorio_local}')
    print(f'Nombre del archivo:\n{nombre_categoria}')

    return

def eliminar_receta(categoria, receta):

    directorio_local = localizacion_recetas/categoria/receta

    archivo = directorio_local.with_suffix('.txt')

    archivo.unlink()


    print(f'El archivo fue eliminado: \n{receta}')
    return

def eliminar_categoria(categoria):
    directorio_local = Path(localizacion_recetas/categoria)

    directorio_local.rmdir()

    print(f'se enimino correctamente: {categoria}')
    return

def main():

    #Bucle que permite que el programa siga ejecutandose
    while True:

        print(f'\n\nTus recetas estan en {localizacion_recetas} ')

        print('Bienvenido')
        print(f'Tienes [{numero_de_recetas()}] Recetas')

        print('''Menu
        1.- Leer Receta
        2.- Crear Receta
        3.- Crear categoria
        4.-Eliminar receta
        5.-eliminar categoria
        6.- finalizar programa''')

        op = int(input())

        match op:
            case 1:
                categoria = elegir_categoria()
                receta = elegir_recetas(categoria)
                leer_receta(categoria, receta)
            case 2:
                categoria = elegir_categoria()
                crear_receta(categoria)
            case 3:
                crear_categoria()
            case 4:
                categoria = elegir_categoria()
                receta = elegir_recetas(categoria)
                eliminar_receta(categoria, receta)
            case 5:
                categoria = elegir_categoria()
                eliminar_categoria(categoria)
            case 6:
                return False
            case _:
                print("\nNo tontito, es un numero entre 1 y 6 \n")
        input('Pulsa ENTER para regresar al menu...')

        system('cls')
        continue

    return

main()
