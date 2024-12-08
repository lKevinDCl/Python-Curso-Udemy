class Pajaro:
    #Atributos de la clase
    alas = True

    'Metodos de instancia'
    #Este es un contructor
    #Atributos de un objeto
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pajaro a volado {metros} metros')
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es : {self.color}')

    'Metodo de clase'
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} de huevos')
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print('El pajaro mira')


piolin = Pajaro ('Amarillo','Canario')

piolin.alas = False
#piolin.volar(50)
#piolin.pintar_negro()
print(piolin.alas)

'Metodo de clase'
Pajaro.poner_huevos(3)

'Metodo estaico'
Pajaro.mirar()

'Ejercicio 1'

'''
Práctica Tipos de Métodos 1
Crea un método estático respirar() para la clase Mascota. Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"
'''


class Mascota():

    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")


Mascota.respirar()

'Ejercicio 2'
'''
Práctica Tipos de Métodos 2
Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.
'''


class Jugador():
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True

'Ejercicio 3'

'''
Práctica Tipos de Métodos 3
Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una instancia de Personaje, que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.
'''


class Personaje():

    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1