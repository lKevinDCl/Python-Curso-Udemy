#   Programar el juego del ahorcado
#   6 vidas
#   Aegurarse que solo se introduzcan letras
#   utilizar funciones muchisisismas
#   Las palabras las debo establecer yo y adivinarlas

# 1.- El sistema debe elegir una palabra
# 2.- Sistema le pide al usuario una letra
# 3.- El sistema debe validad si el input es una letra
# 4.- Se busca dicha letra dentro de la palabra seleccionada con Choice
# 5.- Si la letra es verdadera se mostrara los espacios de la palabra
#     Sino se resta una vida y se muestra los espacios vacios por adivinar
# 6- Si se logra mandar "Completaste la palabra secreta" {vidas restantes} sino "Game Over"

'Libreria random'
from random import choice #La libreria random permite escoger una palabra aleatoria de la lisat

'Libreria re'
import re
from re import match

'Lista de palabras'
lista = ['Gato', 'Sobremesa', 'Arbol', 'Otorrinolaringologo','Sol','uwu'] #Es una lista dada por el sistema

'Funcion para escoger una palabra al azar de la lista realizada'
def escoger_palabra(lista_palabras):
    #guardamos en la variable palabra el string de la palabra elegida en nuestra lista
    palabra = str(choice(lista_palabras))

    #Retornamos la palabra en minuscula para evitar errores
    return palabra.lower()

'Funcion devuelve la longitud de la palabra'
def longitud_palabra(palabra_secreta):
    # Guardamos en la variable espacios la longitud de nuestro string
    espacios = len(palabra_secreta)

    # Retornamos la cantidad de espacios que se encuentra en el string
    return espacios

'Funcion que permite si el input es correcto y devuelve una lista con la letra o letras enviadas.'
def dar_letra():
    # Guardamos dentro de la variable letra_palabra la insercion dada por el usuario  y lo ponemos en minusculas para
    # evitar errores
    letra_palabra = input('Dame una letra o palabra: ').lower()

    # La letra o palabra debe ser si o si un str de tipo texto, y no numerico.
    # Hacemos uso de la libreria re; nos permite validar que mientras el dato dado sea (A-Z,a-z)
    # Va a devolver True de lo contrario devolvera False y el bucle continuara de forma indeterminada
    # Hasta que arroje un tipo de dato valido

    patron = re.compile(r'^[a-zA-Z]+$')

    #Dentro del bucle while inicializamos que mientras el valor dado por el usuarios sea
    #diferente a los que esperamos siempre se va a ejecutar hasta que se ingrese un valor correcto
    while not patron.match(letra_palabra):
        print("\n*Dame una letra o palabra sin caracteres especiales/numeros*")
        letra_palabra = input('\nDame una letra o palabra: ') #Actualizamos el valor para salir del bucle

    # Conversitimos el str en una lista en caso de que hayan sido muchos valores los insertados
    lista_letras = list(letra_palabra)

    #Retornamos la lista de letras
    return lista_letras

'Funcion que devuelve los espacios acertados'
def comparar_letra_con_palabra(lista_letras, palabra_secreta):

    # Guardamos en la variable una lista del string de palabra secreta
    lista_palabra_secreta = list(palabra_secreta)

    #Inicializamos una variable de tipo lista como vacia
    lista_espacios = []

    # loop que recorre a lista_palabra_secreta
    #  pa identificar si de la "lista_letras" hay concordancia
    # Si si, entonce remplaza el espacio vacio par la letra
    # Sino entonces lo recllena con un espacio vacio '_'
    for i in lista_palabra_secreta:

        if i in lista_letras:
            lista_espacios.append(i)
        else:
            lista_espacios.append('_')

    #Se retorna la cantidad de aciertos con sus respectivos espacios vacios
    return lista_espacios

'Funcion que permite averiguar si dentro de la palabra se encuentran los aciertos nuevos dados por el usuario'
def intento(palabra_secreta,nuevos_aciertos):

    # Loop que se encarga de recorrer nuevos_aciertos
    # y verificar si estos se encuentran dentro de palabra secreta

    #Esto ayuda a determinar si el usuario pierde una vida o no
    for letra in nuevos_aciertos:
         if letra in palabra_secreta:
             return True
    return  False

'Funcion que permite actualizar la lista de aciertos'
def actualizar_lista_aciertos(lista_aciertos, nuevos_aciertos):

    # Se crea un loop que recorra la longitud de la lista_aciertos
    for i in range(len(lista_aciertos)):

        # Si la lista aciertos es igaul a '_'
        # Entonces en lista acierto sustituimos el valor en i el nuevo_acierto en i

        if lista_aciertos[i] == '_': # Asumiendo que los aciertos no descubiertos están representados por '_' lista_aciertos[i] = nuevos_aciertos[i]
            lista_aciertos[i] = nuevos_aciertos[i]

    # Retornamos los aciertos actualizados para que se vuelva a reutilizar
    return lista_aciertos

'Funcion que permite comprobar si la palabra completada es igual a la palabra secreta y finalizar el juego'
def comprobar_palabra_completa(lista_aciertos, palabra_secreta):

    # Como habiamos utilizado con anterioridad listas, hay que pasar esas listas a str
    # Entonces utilizamos el .join para unir nuestra lista lista y guardarla en texto_completo
    texto_completo = ''.join(lista_aciertos)

    # Si el texto_completo hace match con palabra_secreta
    # Entonces el jeugo termino
    # Sino el jeugo continua
    if texto_completo == palabra_secreta:
        return True
    else:
        return False

'funcion principal'
def play():

    'Variable que aloja la palabra secreta'
    palabra_secreta = escoger_palabra(lista)
    #print(palabra_secreta) #Me permite saber la palabra secreta para testeo

    'Variable que aloja la longitud de la pabra secreta'
    long_palabra = longitud_palabra(palabra_secreta)

    # Inicializar la lista de aciertos con guiones bajos
    lista_aciertos = ['_'] * long_palabra

    #Le permite al usuario visualizar que tan grande es la pregunta
    print(lista_aciertos)

    #Cantidad de vidas
    intentos = 6

    while intentos > 0:

        'variable para almacenar el dato dado por el usuario'
        lista_letras = dar_letra()

        'Variable para almacenar la cantidad de aciertos en el intento n '
        nuevos_aciertos = comparar_letra_con_palabra(lista_letras, palabra_secreta)

        'Variable que guarda la actualizacion entre la lista de aciertos anterior y la nueva'
        lista_aciertos = actualizar_lista_aciertos(lista_aciertos, nuevos_aciertos)

        'Muestra al usuario sus aciertos y los "_" espacios a adivinar'
        print(lista_aciertos)

        '''
            Si la funcion intento verifica que los nuevos_aciertos no se encuentrasn
            en la palabra secreta, entonces le quita una vida al jugador hasta que se agoten y salga del
            loop while y mande el mensaje Game Over
            
            Pero si si se encuentran estas letras entonces hay que comprobar
            si la palabra fue resuelta. si si, entonces termina el juego, sino simplemente se repite el loop 
        '''
        if intento(palabra_secreta,nuevos_aciertos):
            if comprobar_palabra_completa(lista_aciertos, palabra_secreta):
                return print("Felicidades completaste el juego")
            else:
                pass
        else:
            intentos -= 1
            print(f'te quedan {intentos} intentos')

    if intentos == 0:
        return print("Game Over :(")

    #Simplemente detiene la ejecucion de la funcion
    return

#Mandamos a ejecutar solo nuestra funcion play que engloba al resto de funciones
play()

'''
NOTAS: 
Esta practica me ayudo mucho a mejorar mi logica como programador.
si bien es cierto que muchas de las cosas que implemente mediante librerias, no sabia muy bien como escribirlas. 
entiendo el flujo de trabajo de mi sistema.

Me enfrente a varios problemas. entre ellos, el tratar de actualizar una lista con nuevos iteradores sin remplazar los que aun no
habian sido descubiertos

Otro de mis retos fue la de checar si de mi lista intentos hacia match con la lista de palabra secreta, para identificar si el usuario 
habia dado una respuesat correcta o incorrecta para hayas la palabra secreta

Finalmente si bien aprendi a mejorar mi flujo de trabajo
me llevo un sabor agridulce, ya que los ultimos detalles tuve que depender de  investigar por mi propia cuenta
y si bien encontraba la solucion, no sentia que fuese un logro realmente mio.

pero quien diria que a programar se aprende programando :D
'''


