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

