"""

Código principal

"""

from numeros import decoradores, generadores

def main():


    generador_perfumes = generadores.generador_turno_perfumes()
    generador_farmacia = generadores.generador_turno_farmacia()
    generador_cosmeticos = generadores.generador_turno_cosmeticos()

    while True:
        print('''Bienvenido
        ¿Qué area desea visitar?''')
        print('''
        [1] Perfumes
        [2] Farmacia
        [3] Cosmeticos
        [0] Salir''')
        op = int(input())

        match op:
            case 1:
                decoradores.decorador_turno(generador_perfumes)
                continue
            case 2:
                decoradores.decorador_turno(generador_farmacia)
                continue
            case 3:
                decoradores.decorador_turno(generador_cosmeticos)
                continue
            case _:
                return False

main()