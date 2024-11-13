'''
def suma(**kwargs):

    total = 0

    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor

    return total

print(suma(x=3,y=5,z=2))
'''
from itertools import count
from wsgiref.validate import validator


def prueba(num1, num2, *args, **kwargs):

    print(f"el primer valor es: {num1}")
    print(f"el segundo valor es: {num2}")

    for arg in args:
        print(f'args = {args}')


    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')

args = [100,200,300,400]
kwargs = {'x': 'uno', 'y':'dos', 'z':'tres'}

prueba(15,50, *args,**kwargs)


'''
Práctica sobre Argumentos Indefinidos (**kwargs) 1
Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.
'''

#cantidad_atributos() got an unexpected keyword argument 'color_ojos'
def cantidad_atributos(**kwargs):

    contador = 0
    for arg in kwargs:
        contador += 1

    return contador

print(cantidad_atributos(x=1,y=2,z=3))


'''
Práctica sobre Argumentos Indefinidos (**kwargs) 2
Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados
en forma de palabras clave (keywords). 
La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
'''

#dict_keys(['color_ojos', 'color_pelo']) != ['azules', 'rubio'] : La función cantidad_atributos no arroja los resultados esperados para una prueba con 2 argumentos entregados
#dict_values(['azules', 'rubio']) != ['azules', 'rubio'] : La función cantidad_atributos no arroja los resultados esperados para una prueba con 2 argumentos entregados

def lista_atributos(**kwargs):

    return list(kwargs.values())

#kwargs1 = {'color_ojos':'azules','color_pelo':'rubio'}

print(lista_atributos(color_ojos='azules',color_pelo='rubio'))


'''
Práctica sobre Argumentos Indefinidos (**kwargs) 3
Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

Características de María:
color_ojos: azules
'''

def describir_persona(nombre, **kwargs):

    print(f'Características de {nombre}:')


    for nombre_argumento, valor_argumento in kwargs.items():

        print(f'{nombre_argumento}: {valor_argumento}')

    return

print(describir_persona('kevin', color_ojos='azules',color_pelo='rubio'))
