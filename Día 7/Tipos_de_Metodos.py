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
