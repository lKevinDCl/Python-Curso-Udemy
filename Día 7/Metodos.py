class Pajaro:
    #Atributos de la clase
    alas = True

    #Este es un contructor
    #Atributos de un objeto
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pajaro a volado {metros} metros')

piolin = Pajaro ('Amarillo','Canario')

piolin.piar()
piolin.volar(10)

'ejercicio 1'

'''
Práctica Métodos 1
Crea una clase Perro. Dicho perro debe poder ladrar.

Crea el método ladrar() y ejecútalo en una instancia de Perro. Cada vez que ladre, debe mostrarse en pantalla "Guau!".
'''

class Perro():

    def ladrar(self):
        print('Guau!')

mi_perro = Perro()

mi_perro.ladrar()

'ejercicio 2'

'''
Práctica Métodos 2
Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() (deberá imprimir "¡Abracadabra!").

Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.
'''


class Mago():

    def lanzar_hechizo(self):
        print('¡Abracadabra!')


merlin = Mago()

merlin.lanzar_hechizo

'ejercicio 3'

'''

Práctica Métodos 3
Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje

"La alarma ha sido pospuesta {cantidad_minutos} minutos"
'''


class Alarma():

    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")


mi_alarma = Alarma()

mi_alarma.postergar(15)
