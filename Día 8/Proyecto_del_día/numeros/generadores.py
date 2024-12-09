"""

Generadores turnos

"""

def generador_turno_perfumes():
    """
    Generador de turnos Perfumes
    :return:
    """
    turno = 0
    while True:
        turno += 1
        yield f' P - {turno} '

def generador_turno_farmacia():
    """
    generador de turnos Farmacia
    :return:
    """
    turno = 0
    while True:
        turno += 1
        yield f' F - {turno} '

def generador_turno_cosmeticos():
    """
    Generador de turnos Cosmeticos
    :return:
    """
    turno = 0
    while True:
        turno += 1
        yield f' C - {turno} '

