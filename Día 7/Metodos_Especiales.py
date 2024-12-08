'''mi_lista = [1,1,1,1,1,1,1,1]

print (mi_lista)

class Objeto:
    pass

mi_objeto = Objeto()

print(mi_objeto)'''

class Cd:
    def __init__(self, autor,titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    #Es un metodo especial que permite la forma en la cual se leera el objeto cuando se traiga su str
    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'

    #Se establece como se ejecutara el largo en el objeto
    def __len__(self):
        return  self.canciones

    def __del__(self):
        print('Se ha eliminado el cd')

mi_cd = Cd('Pink Floyd', 'The Wall', 24)

print (len(mi_cd))

del mi_cd #Elimina la instancia

'Ejercicio 1'

'''
Práctica Métodos Especiales 1
Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima el objeto, devuelva '"{titulo}", de {autor}' (atención: el título debe estar encerrado entre comillas dobles).
'''


class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self, ):
        return f'"{self.titulo}", de {self.autor}'


'Ejercicio 2'

'''
Práctica Métodos Especiales 2
Dada la clase Libro, implementa el método especial __len__ para que cada vez que se ejecute la función len() sobre el mismo, devuelva el número de páginas como número entero.
'''

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas

    'Ejercicio 3'

    '''
    Práctica Métodos Especiales 3
Dada la clase Libro, implementa el método especial __del__ para que el usuario sea informado con el mensaje "Libro eliminado", mostrándolo en pantalla cada vez que el libro se elimine.
    '''

    class Libro():
        def __init__(self, titulo, autor, cantidad_paginas):
            self.titulo = titulo
            self.autor = autor
            self.cantidad_paginas = cantidad_paginas

        def __del__(self):
            print('Libro eliminado')