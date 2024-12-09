import unittest
from numeros import decoradores, generadores

class ProbarGeneradores(unittest.TestCase):
    """
    Se realiza una función de testeo
    """
    def test_opcion(self):
        generador = generadores.generador_turno_farmacia()
        resultado = next(generador)
        self.assertEqual(resultado, ' F - 1 ')

class ProbarDecoradores(unittest.TestCase):
    """
    Se realiza una función de testeo
    """

    def test_opcion(self):
        turno = generadores.generador_turno_perfumes()
        decorador = decoradores.decorador_turno(turno)
        resultado = decorador()
        self.assertEqual(resultado, 'Su turno es:\n P - 1 \nAguarde y\nsera atendido')

if __name__ == '__main__':
    unittest.main()
