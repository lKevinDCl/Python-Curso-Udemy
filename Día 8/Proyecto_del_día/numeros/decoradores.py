"""
Decorador Turnos
"""
def decorador_turno(objeto_generador):
    """
    Decorador de todos lso turnos
    :param objeto_generador:
    :return:
    """

    g = objeto_generador

    def decorador():
        print('Su turno es:')
        print(next(g))
        print('Guarde y\nsera atendido')

    return decorador()


