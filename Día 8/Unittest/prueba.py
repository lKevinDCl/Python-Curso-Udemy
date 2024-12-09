import unittest
import Cambia_texto

class probarCambiaTexto(unittest.TestCase):

    """
    Se realiza una funcion de testeo
    """
    def test_mayusculas(self):
        palabra = 'Buen dia'
        resultado = Cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'BUEN DIA')


"""
Es una forma de proteger el código y especificarle a python que
funcion de debe ejecutar
"""
if  __name__ == '__main__':
    unittest.main()

